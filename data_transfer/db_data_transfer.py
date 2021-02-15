from data_transfer.data_storage_interface import DataStorageInterface
from model.motor_calc import MotorCalc
from model.losses import LossType
from db.queries import Queries


class DBDataTransfer(DataStorageInterface):
    @staticmethod
    def init_database():
        Queries.init_db()

    @staticmethod
    def export_data(data: MotorCalc):
        vals_to_insert = (data.limit, data.Ps, data.PAl, data.Pss, data.Pp)
        Queries.insert_into_motor_results_table(vals_to_insert)
        id_added = Queries.getLastID(table_name="MotorResults")
        print(id_added)

        losses_pssv, losses_ppv = data.rotor_losses()
        losses_psv, losses_palv = data.stator_losses()

        Queries.insert_into_loss_table(loss_type=LossType.LOSS_PSS, losses=losses_pssv, id_to_add=id_added)
        Queries.insert_into_loss_table(loss_type=LossType.LOSS_PP, losses=losses_ppv, id_to_add=id_added)
        Queries.insert_into_loss_table(loss_type=LossType.LOSS_PS, losses=losses_psv, id_to_add=id_added)
        Queries.insert_into_loss_table(loss_type=LossType.LOSS_PAL, losses=losses_palv, id_to_add=id_added)
        return id_added

    @staticmethod
    def import_data(id: int):
        limit, Ps, PAl, Pss, Pp = Queries.get_from_motor_results_table(id)
        losses_pssv = Queries.get_from_loss_table(loss_type=LossType.LOSS_PSS, id=id)
        losses_ppv = Queries.get_from_loss_table(loss_type=LossType.LOSS_PP, id=id)
        losses_psv = Queries.get_from_loss_table(loss_type=LossType.LOSS_PS, id=id)
        losses_palv = Queries.get_from_loss_table(loss_type=LossType.LOSS_PAL, id=id)
        stator_losses = losses_psv, losses_palv
        rotor_losses = losses_pssv, losses_ppv
        return limit, Ps, PAl, Pss, Pp, stator_losses, rotor_losses
