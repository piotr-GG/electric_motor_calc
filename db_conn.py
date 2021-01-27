import sqlite3
import os.path


class NoSuchTableError(sqlite3.OperationalError):
    def __init__(self):
        super().__init__()
        self.args = ("No such table in DB",)


class DBCreationError(BaseException):
    pass


# TODO: REORGANIZE THIS CLASS
class DBConnection:
    def __init__(self, db_path):
        if os.path.isfile(db_path):
            self.__conn = sqlite3.connect(db_path)
            self.__c = self.__conn.cursor()
        else:
            if not self.create_db(db_path):
                raise DBCreationError

    @property
    def conn(self):
        return self.__conn

    @conn.setter
    def conn(self, value):
        if isinstance(value, sqlite3.Connection):
            self.__conn = value
        else:
            raise ValueError("Wrong argument for conn class attribute!")

    @property
    def c(self):
        return self.__c

    def create_db(self, db_path) -> bool:
        open(db_path, 'w').close()
        self.__conn = sqlite3.connect(db_path)
        self.__c = self.conn.cursor()

        stmt = '''CREATE TABLE MotorResults (ID INTEGER PRIMARY KEY AUTOINCREMENT, limits INTEGER NOT NULL, 
                Ps REAL NOT NULL, PAl REAL NOT NULL, Pss REAL NOT NULL, Pp REAL NOT NULL) '''
        self.c.execute(stmt)
        self.conn.commit()
        return True

    def close_conn(self):
        self.__conn.close()

    def createResultTable(self):
        stmt = '''CREATE TABLE MotorResults (ID INTEGER PRIMARY KEY AUTOINCREMENT, limits INTEGER NOT NULL, 
                Ps REAL NOT NULL, PAl REAL NOT NULL, Pss REAL NOT NULL, Pp REAL NOT NULL) '''
        self.c.execute(stmt)

    def insertValuesIntoResultTable(self):
        stmt = '''INSERT INTO MotorResults (limits, Ps, PAl, Pss, Pp) VALUES 
                  ( ?, ?, ?, ?, ?)'''
        vals = [(6, 5, 5, 10, 15.4),
                (2, 4, 4.5, 3.2, 47),
                (66, 10, 3.2, 1.5, 43.2)]

        self.c.executemany(stmt, vals)

    def insertValueIntoMotorResults(self, value: tuple):
        if not self.tableExists("MotorResults"):
            self.createResultTable()

        stmt = '''INSERT INTO MotorResults (limits, Ps, PAl, Pss, Pp) VALUES
                  (?, ?, ?, ?, ?)'''
        self.c.execute(stmt, value)
        self.conn.commit()

    def getResults(self):
        stmt = '''SELECT * FROM MotorResults'''
        return self.c.execute(stmt).fetchall()

    def getSingleResult(self, id: int):
        """
        :param id: id of result stored in DB
        :returns: tuple with query results
        :raises NoSuchTableError: when no table is present in DB by given name
        :raises ValueError: when supplied value is invalid
        """
        if id > 0:
            try:
                stmt = '''SELECT * FROM MotorResults WHERE ID = ?'''
                return self.c.execute(stmt, (id,)).fetchone()
            except sqlite3.OperationalError as e:
                if "no such table" in e.args[0]:
                    raise NoSuchTableError()
        else:
            raise ValueError("ID < 0 !")

    def tableExists(self, tbl_name: str) -> bool:
        """
        :param tbl_name: name of table to be checked
        :returns: bool
        """
        stmt = "SELECT COUNT(*) FROM sqlite_master WHERE type = ? AND name = ?"
        return self.c.execute(stmt, ("table", tbl_name)).fetchone()[0] >= 1


if __name__ == "__main__":
    db_test = DBConnection('db/results.db')
    # db_test.createResultTable()
    # db_test.insertValuesIntoResultTable()
    # for row in db_test.getResults():
    #     print(row)
    # print("*" * 50)
    # db_test.insertValuesIntoResultTable()
    print(db_test.getSingleResult(2))
    print(db_test.getResults())

    # print(db_test.tableExists("MotorResults"))
    # db_test.insertValue((5, 55, 23.3, 23.4, 21))
    # for row in db_test.getResults():
    #     print(row)

    db_test.conn.commit()
    db_test.conn.close()
