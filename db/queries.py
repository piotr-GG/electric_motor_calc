from db.losses_record_builder import LossesRecordBuilder
from db.db_conn import DBConnection, DBCreationError
from model.flux_density import FluxType, FluxDensity
from model.losses import Losses, LossType
from db.fluxes_record_builder import FluxesRecordBuilder


# TODO: ADD TRY EXCEPT CLAUSES FOR SQLITE3 EXCEPTIONS
class Queries:
    db_path = "db/results.db"

    @classmethod
    def init_db(cls):
        try:
            cls.tableExists("MotorResults")
            print("DB ISTNIEJE!")
        except DBCreationError:
            print("NIE ISTNIEJE. TRZEBA UTWORZYĆ!")

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
        stmt = '''INSERT INTO MotorResults (limits, kls, klr, gs, gr, Ps, PAl, Pss, Pp) VALUES (?, ?, ?, ?, ?, ?, ?, 
        ?, ?) '''
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
        stmt = f'''INSERT INTO "{tbl_name}" ("order", "value", "result_ID") VALUES ( ?, ? , ?)'''
        with DBConnection(Queries.db_path) as db:
            db.executemany(stmt, vals)

    @classmethod
    def insert_into_flux_table(cls, flux_type: FluxType, fluxes: FluxDensity, id_to_add: int):
        tbl_name = ""
        if flux_type == FluxType.StatorFlux:
            tbl_name = "stator_fluxes"
        elif flux_type == FluxType.RotorFlux:
            tbl_name = "rotor_fluxes"
        else:
            raise ValueError("Wrong value for flux_type argument!")
        vals = FluxesRecordBuilder.build_record(fluxes, id_to_add)
        stmt = f'''INSERT INTO "{tbl_name}" ("order", "value", "result_ID") VALUES ( ?, ?, ?)'''
        with DBConnection(Queries.db_path) as db:
            db.executemany(stmt, vals)

    @classmethod
    def get_from_motor_results_table(cls, id: int):
        if id > 0:
            stmt = '''SELECT "limits", "kls", "klr", "gs", "gr", "Ps", "PAl", "Pss", "Pp" FROM MotorResults WHERE ID 
            = ? '''
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
            raise ValueError("get_from_loss_table()\nWrong value for loss_type argument!")
        stmt = f'''SELECT * FROM "{tbl_name}" WHERE "result_ID" = ?'''
        with DBConnection(Queries.db_path) as db:
            db.execute(stmt, (id,))
            return LossesRecordBuilder.parse_record(db.fetchall())

    @classmethod
    def get_from_flux_table(cls, flux_type: FluxType, id: int):
        tbl_name = ""
        if flux_type == FluxType.StatorFlux:
            tbl_name = "stator_fluxes"
        elif flux_type == FluxType.RotorFlux:
            tbl_name = "rotor_fluxes"
        else:
            raise ValueError("get_from_flux_table()\nWrong value for flux_type argument!")
        stmt = f'''SELECT * FROM {tbl_name} WHERE "result_ID" = ?'''
        with DBConnection(Queries.db_path) as db:
            db.execute(stmt, (id,))
            return FluxesRecordBuilder.parse_record(db.fetchall())

    @classmethod
    def get_available_ids(cls):
        stmt = f'''SELECT "ID" From "MotorResults"'''
        with DBConnection(Queries.db_path) as db:
            db.execute(stmt)
            return db.fetchall()


if __name__ == "__main__":
    Queries.init_db()
    print(list(x[0] for x in Queries.get_available_ids()))
    print(Queries.getLastID("MotorResults"))
    # print(Queries.get_from_loss_table(LossType.LOSS_PSS, 34))
    #
    # print(Queries.get_from_motor_results_table(34))
    # motor = Motor()
    # motorCalc = MotorCalc(motor, limit=5)
    # motorCalc.calculate()
