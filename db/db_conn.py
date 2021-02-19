import sqlite3
import os.path

from model.motor import Motor
from model.motor_calc import MotorCalc
from definitions import ROOT_DIR


class NoSuchTableError(sqlite3.OperationalError):
    def __init__(self):
        super().__init__()
        self.args = ("No such table in DB",)


class DBCreationError(BaseException):
    pass


class DBConnection:
    def __init__(self, db_path):
        db_path = ROOT_DIR + "/" + db_path
        if os.path.isfile(db_path):
            self._conn = sqlite3.connect(db_path)
            self._cursor = self._conn.cursor()
        else:
            if not self.create_db(db_path):
                raise DBCreationError

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    @property
    def connection(self):
        return self._conn

    @property
    def cursor(self):
        return self._cursor

    def commit(self):
        self.connection.commit()

    def close(self, commit=True):
        if commit:
            self.commit()
        self.connection.close()

    def execute(self, sql, params=None):
        self.cursor.execute(sql, params or ())

    def executemany(self, sql, params):
        self.cursor.executemany(sql, params)

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.fetchall()

    def query_multiple(self, sql, param_list):
        self.cursor.executemany(sql, param_list)
        return self.fetchall()

    def create_db(self, path):
        with sqlite3.connect(path) as db:
            self._conn = sqlite3.connect(path)
            self._cursor = self._conn.cursor()
            # MotorResults table
            stmt = '''CREATE TABLE MotorResults (ID INTEGER PRIMARY KEY AUTOINCREMENT, limits INTEGER NOT NULL, 
            kls INTEGER NOT NULL, klr INTEGER NOT NULL, gs INTEGER NOT NULL, gr INTEGER NOT NULL, Ps REAL NOT NULL, 
            PAl REAL NOT NULL, Pss REAL NOT NULL, Pp REAL NOT NULL) '''
            self.execute(stmt)
            # Pss_losses table
            stmt = '''CREATE TABLE "Pss_losses" (
                    "ID"	INTEGER,
                    "order"	INTEGER,
                    "value"	REAL NOT NULL,
                    "result_ID"	INTEGER,
                    PRIMARY KEY("ID" AUTOINCREMENT),
                    FOREIGN KEY("result_ID") REFERENCES "MotorResults" ("ID"))
                            '''
            self.execute(stmt)
            # Pp_losses table
            stmt = '''CREATE TABLE "Pp_losses" (
                    "ID"	INTEGER,
                    "order"	INTEGER,
                    "value"	REAL NOT NULL,
                    "result_ID"	INTEGER,
                    PRIMARY KEY("ID" AUTOINCREMENT),
                    FOREIGN KEY("result_ID") REFERENCES "MotorResults" ("ID"))
                    '''
            self.execute(stmt)
            # Ps_losses
            stmt = '''CREATE TABLE "Ps_losses" (
                    "ID"	INTEGER,
                    "order"	INTEGER,
                    "value"	REAL NOT NULL,
                    "result_ID"	INTEGER,
                    PRIMARY KEY("ID" AUTOINCREMENT),
                    FOREIGN KEY("result_ID") REFERENCES "MotorResults" ("ID"))
                    '''
            self.execute(stmt)
            # PAL_losses
            stmt = '''CREATE TABLE "PAl_losses" (
                    "ID"	INTEGER,
                    "order"	INTEGER,
                    "value"	REAL NOT NULL,
                    "result_ID"	INTEGER,
                    PRIMARY KEY("ID" AUTOINCREMENT),
                    FOREIGN KEY("result_ID") REFERENCES "MotorResults" ("ID"))
                    '''
            self.execute(stmt)
            # stator_fluxes
            stmt = '''CREATE TABLE "stator_fluxes" (
                    "ID"	INTEGER,
                    "order"	INTEGER,
                    "value"	REAL NOT NULL,
                    "result_ID"	INTEGER,
                    PRIMARY KEY("ID" AUTOINCREMENT),
                    FOREIGN KEY("result_ID") REFERENCES "MotorResults" ("ID"))
                    '''
            db.execute(stmt)
            # rotor_fluxes
            stmt = '''CREATE TABLE "rotor_fluxes" (
                                "ID"	INTEGER,
                                "order"	INTEGER,
                                "value"	REAL NOT NULL,
                                "result_ID"	INTEGER,
                                PRIMARY KEY("ID" AUTOINCREMENT),
                                FOREIGN KEY("result_ID") REFERENCES "MotorResults" ("ID"))
                                '''
            db.execute(stmt)
        return True

if __name__ == "__main__":
    from data_transfer.db_data_transfer import DBDataTransfer

    motor = Motor()
    motorCalc = MotorCalc(motor, limit=5)
    motorCalc.calculate()

    id_added = DBDataTransfer.export_data(motorCalc)
    losses_Pss, losses_Pp, losses_Ps, losses_PAl = DBDataTransfer.import_data(id_added)
    print(losses_Pss)
