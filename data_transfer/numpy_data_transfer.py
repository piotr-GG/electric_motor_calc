from data_transfer.data_storage_interface import DataStorageInterface
from model.motor_calc import MotorCalc
from model.motor import Motor
from model.motor_results import MotorResults
from definitions import ROOT_DIR
import numpy as np


class NumpyDataTransfer(DataStorageInterface):
    @staticmethod
    def export_data(data: MotorCalc, destination: str) -> bool:
        limit = data.limit
        kls = data.kls_
        klr = data.klr_
        gs = data.gs_
        gr = data.gr_
        Ps = data.Ps
        PAl = data.PAl
        Pss = data.Pss
        Pp = data.Pp
        losses_pssv, losses_ppv = data.rotor_losses()
        losses_psv, losses_palv = data.stator_losses()

        kwargs = {"limit": limit, "kls": kls, "klr": klr, "gs": gs, "gr": gr, "Ps": Ps, "PAl": PAl, "Pss": Pss,
                  "Pp": Pp, "losses_pssv": losses_pssv,
                  "losses_ppv": losses_ppv, "losses_psv": losses_psv, "losses_palv": losses_palv}
        destination = destination + ".npz" if not destination.endswith(".npz") else destination
        path = ROOT_DIR + "/npz/" + destination
        np.savez(path, **kwargs)
        return True

    @staticmethod
    def import_data(destination: str):
        destination = destination + ".npz" if not destination.endswith(".npz") else destination
        # path = ROOT_DIR + "/npz/" + destination
        with np.load(destination, allow_pickle=True) as data_loaded:
            limit = data_loaded["limit"]
            kls = data_loaded["kls"]
            klr = data_loaded["klr"]
            gs = data_loaded["gs"]
            gr = data_loaded["gr"]
            Ps = data_loaded["Ps"]
            PAl = data_loaded["PAl"]
            Pss = data_loaded["Pss"]
            Pp = data_loaded["Pp"]
            losses_ppv = data_loaded["losses_ppv"]
            losses_psv = data_loaded["losses_psv"]
            losses_palv = data_loaded["losses_palv"]
            losses_pssv = data_loaded["losses_pssv"]

            stator_losses = losses_psv, losses_palv
            rotor_losses = losses_pssv, losses_ppv
        return limit, kls, klr, gs, gr, Ps, PAl, Pss, Pp, stator_losses, rotor_losses


if __name__ == "__main__":
    m = Motor()
    m_calc = MotorCalc(m, limit=15)
    m_calc.calculate()
    m_res = MotorResults(m_calc)
    NumpyDataTransfer.export_data(m_calc, "no_jak_tam_2.npz")
    limit, Ps, PAl, Pss, Pp, losses_ppv, losses_psv, losses_palv, losses_pssv = NumpyDataTransfer.import_data(
        "no_jak_tam_2.npz")
    print(losses_palv)
