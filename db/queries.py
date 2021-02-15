from db.losses_record_builder import LossesRecordBuilder
from db.db_conn import DBConnection
from model.losses import Losses, LossType


class Queries:
    db_path = "db/results.db"

    @classmethod
    def init_db(cls):
        if cls.tableExists("MotorResults") and cls.tableExists("Pss_losses") and cls.tableExists("Ps_losses") \
                and cls.tableExists("PAl_losses") and cls.tableExists("Pp_losses"):
            print("DB ISTNIEJE!")
        else:
            cls.create_db(cls.db_path)
            print("NIE ISTNIEJE. TRZEBA UTWORZYĆ!")

    @classmethod
    def create_db(cls):
        with DBConnection(cls.db_path) as db:
            # MotorResults table
            stmt = '''CREATE TABLE MotorResults (ID INTEGER PRIMARY KEY AUTOINCREMENT, limits INTEGER NOT NULL, 
                            Ps REAL NOT NULL, PAl REAL NOT NULL, Pss REAL NOT NULL, Pp REAL NOT NULL) '''
            db.execute(stmt)
            # Pss_losses table
            stmt = '''CREATE TABLE "Pss_losses" (
                    "ID"	INTEGER,
                    "order"	INTEGER,
                    "value"	REAL NOT NULL,
                    "result_ID"	INTEGER,
                    PRIMARY KEY("ID" AUTOINCREMENT),
                    FOREIGN KEY("result_ID") REFERENCES "MotorResults" ("ID"))
            	            '''
            db.execute(stmt)
            # Pp_losses table
            stmt = '''CREATE TABLE "Pp_losses" (
                    "ID"	INTEGER,
                    "order"	INTEGER,
                    "value"	REAL NOT NULL,
                    "result_ID"	INTEGER,
                    PRIMARY KEY("ID" AUTOINCREMENT),
                    FOREIGN KEY("result_ID") REFERENCES "MotorResults" ("ID"))
                    '''
            db.execute(stmt)
            # Ps_losses
            stmt = '''CREATE TABLE "Ps_losses" (
                    "ID"	INTEGER,
                    "order"	INTEGER,
                    "value"	REAL NOT NULL,
                    "result_ID"	INTEGER,
                    PRIMARY KEY("ID" AUTOINCREMENT),
                    FOREIGN KEY("result_ID") REFERENCES "MotorResults" ("ID"))
                    '''
            db.execute(stmt)
            # PAL_losses
            stmt = '''CREATE TABLE "PAl_losses" (
                    "ID"	INTEGER,
                    "order"	INTEGER,
                    "value"	REAL NOT NULL,
                    "result_ID"	INTEGER,
                    PRIMARY KEY("ID" AUTOINCREMENT),
                    FOREIGN KEY("result_ID") REFERENCES "MotorResults" ("ID"))
                    '''
            db.execute(stmt)

    @classmethod
    def tableExists(cls, tbl_name: str) -> bool:
        with DBConnection(Queries.db_path) as db:
            stmt = "SELECT COUNT(*) FROM sqlite_master WHERE type = ? AND name = ?"
            db.execute(stmt, ("table", tbl_name))
            return db.fetchone()[0] >= 1

    @classmethod
    def getLastID(cls, table_name):
        stmt = f"SELECT MAX(\"ID\") FROM {table_name}"
        with DBConnection(Queries.db_path) as db:
            db.execute(stmt)
            return db.fetchone()[0]

    @classmethod
    def insert_into_motor_results_table(cls, value: tuple):
        stmt = '''INSERT INTO MotorResults (limits, Ps, PAl, Pss, Pp) VALUES (?, ?, ?, ?, ?)'''
        with DBConnection(Queries.db_path) as db:
            db.execute(stmt, value)

    @classmethod
    def insert_into_loss_table(cls, loss_type: LossType, losses: Losses, id_to_add: int):
        tbl_name = ""
        if loss_type == LossType.LOSS_PP:
            tbl_name = "Pp_losses"
        elif loss_type == LossType.LOSS_PS:
            tbl_name = "Ps_losses"
        elif loss_type == LossType.LOSS_PAL:
            tbl_name = "PAl_losses"
        elif loss_type == LossType.LOSS_PSS:
            tbl_name = "Pss_losses"
        else:
            raise ValueError("Wrong value for loss_type argument!")
        vals = LossesRecordBuilder.build_record(losses, id_to_add)
        stmt = stmt = f'''INSERT INTO "{tbl_name}" ("order", "value", "result_ID") VALUES ( ?, ? , ?)'''
        with DBConnection(Queries.db_path) as db:
            db.executemany(stmt, vals)

    @classmethod
    def get_from_motor_results_table(cls, id: int):
        if id > 0:
            stmt = '''SELECT "limits", "Ps", "PAl", "Pss", "Pp" FROM MotorResults WHERE ID = ?'''
            with DBConnection(Queries.db_path) as db:
                db.execute(stmt, (id,))
                return db.fetchone()

    @classmethod
    def get_from_loss_table(cls, loss_type: LossType, id: int):
        tbl_name = ""
        if loss_type == LossType.LOSS_PP:
            tbl_name = "Pp_losses"
        elif loss_type == LossType.LOSS_PS:
            tbl_name = "Ps_losses"
        elif loss_type == LossType.LOSS_PAL:
            tbl_name = "PAl_losses"
        elif loss_type == LossType.LOSS_PSS:
            tbl_name = "Pss_losses"
        else:
            raise ValueError("Wrong value for loss_type argument!")
        stmt = f'''SELECT * FROM "{tbl_name}" WHERE "result_ID" = ?'''
        with DBConnection(Queries.db_path) as db:
            db.execute(stmt, (id,))
            return LossesRecordBuilder.parse_record(db.fetchall())


if __name__ == "__main__":
    Queries.init_db()
    print(Queries.getLastID("MotorResults"))
    print(Queries.get_from_loss_table(LossType.LOSS_PSS, 34))

    print(Queries.get_from_motor_results_table(34))
    # motor = Motor()
    # motorCalc = MotorCalc(motor, limit=5)
    # motorCalc.calculate()
