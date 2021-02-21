from data_transfer.data_storage_interface import DataStorageInterface
from model.flux_density import FluxDensity
from model.losses import Losses
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
        stator_fluxes = data.stator_fluxes()
        rotor_fluxes = data.rotor_fluxes()

        losses_pssv = losses_pssv.to_list()
        losses_ppv = losses_ppv.to_list()
        losses_psv = losses_psv.to_list()
        losses_palv = losses_palv.to_list()
        stator_fluxes = stator_fluxes.to_list()
        rotor_fluxes = rotor_fluxes.to_list()

        kwargs = {"limit": limit, "kls": kls, "klr": klr, "gs": gs, "gr": gr, "Ps": Ps, "PAl": PAl, "Pss": Pss,
                  "Pp": Pp, "losses_pssv": losses_pssv,
                  "losses_ppv": losses_ppv, "losses_psv": losses_psv, "losses_palv": losses_palv,
                  "stator_fluxes": stator_fluxes, "rotor_fluxes": rotor_fluxes}
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
            stator_fluxes = data_loaded["stator_fluxes"]
            rotor_fluxes = data_loaded["rotor_fluxes"]

            losses_ppv = Losses(losses_ppv[0], losses_ppv[1])
            losses_psv = Losses(losses_psv[0], losses_psv[1])
            losses_palv = Losses(losses_palv[0], losses_palv[1])
            losses_pssv = Losses(losses_pssv[0], losses_pssv[1])
            stator_fluxes = FluxDensity(stator_fluxes[0], stator_fluxes[1])
            rotor_fluxes = FluxDensity(rotor_fluxes[0], rotor_fluxes[1])

            stator_losses = losses_psv, losses_palv
            rotor_losses = losses_pssv, losses_ppv
        return limit, kls, klr, gs, gr, Ps, PAl, Pss, Pp, stator_losses, rotor_losses, stator_fluxes, rotor_fluxes


if __name__ == "__main__":
    limit, kls, klr, gs, gr, Ps, PAl, Pss, Pp, stator_losses, rotor_losses, stator_fluxes,\
        rotor_fluxes = NumpyDataTransfer.import_data(ROOT_DIR + "/npz/ks_77_kr_88_gs_99_gr_66.npz")
    print(stator_fluxes.size)
    print(type(rotor_losses[0]))
    print(rotor_losses[0].size)
    print(type(stator_fluxes))
    print(isinstance(stator_fluxes, FluxDensity))
