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
        pass


if __name__ == "__main__":
    from data_transfer.db_data_transfer import DBDataTransfer
    motor = Motor()
    motorCalc = MotorCalc(motor, limit=5)
    motorCalc.calculate()

    id_added = DBDataTransfer.export_data(motorCalc)
    losses_Pss, losses_Pp, losses_Ps, losses_PAl = DBDataTransfer.import_data(id_added)
    print(losses_Pss)
