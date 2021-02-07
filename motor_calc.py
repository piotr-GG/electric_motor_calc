from motor import Motor
from utils import Utils
from flux_density import FluxDensity
from losses import Losses
import numpy as np
import math


def print_var_value(var, name: str):
    print(f"{name} = {var}")


# TODO:
# Replace exising B and vs with FluxDensity() class instances


class MotorCalc:
    """
    Class used to perform calculation on a motor instance.
    """

    def __init__(self, motor: Motor, *, limit: int = 0, kls: int = 5, klr: int = 5, gs: int = 5, gr: int = 5) -> None:
        if not isinstance(motor, Motor):
            raise ValueError("Wrong value in motor arg")

        self.m = motor
        self.limit = limit
        self.calculated_construct_params = False
        self.calculated_stator_fluxes = False
        self.calculated_stator_losses = False
        self.calculated_rotor_params = False
        self.calculated_rotor_flux_dens = False
        self.calculated_rotor_losses = False

        self.kls = kls
        self.klr = klr
        self.gs = gs
        self.gr = gr

        self.init_atts()

    def init_atts(self):
        self.q = None
        self.ts = None
        self.tr = None
        self.taus = None
        self.taur = None
        self.cc = None
        self.deltas = None
        self.gammas = None
        self.kCs = None
        self.deltar = None
        self.gammar = None
        self.kCr = None
        self.kC = None
        self.qc = None
        self.kqv = None

        self.kCv = None
        self.tauQs = None
        self.y = None
        self.kyv = None
        self.ksv = None
        self.kfv = None
        self.ky1 = None
        self.ks1 = None
        self.kq1 = None
        self.kfs = None
        self.Bfv = None
        self.vls = None
        self.x = None
        self.a = None
        self.ms = None
        self.beta = None
        self.kCs = None
        self.gammas = None
        self.Fks = None
        self.Blk = None

        self.rzad_vs = None
        self.sum_Bs = None
        self.vs = None
        self.Bv = None

        self.frv = None
        self.Deltav = None
        self.Bvs = None
        self.Psv = None
        self.Ps = None
        self.ks = None
        self.Bsv = None
        self.PAlv = None
        self.PAl = None

        self.vrp = None
        self.kCv = None

        self.ksvr = None
        self.ksr = None
        self.bsq = None
        self.alfasq = None
        self.ksq = None
        self.kfr = None
        self.Ir = None
        self.Bfvp = None

        self.vrs = None
        self.frs = None
        self.ksvr = None

        self.kCv = None

        self.alfaQv = None
        self.ktr = None
        self.Uicv = None

        self.gammar_teta = None
        self.Rc = None
        self.przekladnia = None
        self.Rc = None
        self.kRv = None
        self.Rpr = None
        self.Rpr = None
        self.Rprv = None
        self.Rcv = None
        self.Ldeltac = None
        self.kX = None

        self.frpodst = None
        self.Lqra01 = None
        self.Lqra01 = None
        self.Lpr = None
        self.Lpr = None
        self.LQrv = None
        self.LQcv = None
        self.Icv = None
        self.Iprv = None
        self.vrlp = None
        self.gammasr = None
        self.Fkr = None
        self.mr = None
        self.betar = None
        self.Blkrp = None
        self.vlrv = None
        self.epsilon = None
        self.B = None
        self.Blrs = None
        self.Bfvrs = None
        self.suma_fr = None
        self.rzad_vr = None
        self.suma_Bvr = None

        self.vr = None
        self.Bvr = None
        self.fsv = None
        self.Pssv = None
        self.Pss = None
        self.kts = None
        self.etarv = None
        self.Btv = None
        self.p0 = None
        self.pk = None
        self.Bk = None
        self.sigmak = None
        self.kappa = None
        self.xp = None
        self.ppv = None
        self.Ppv = None
        self.Pp = None

    def calculate(self):
        """
        Performs the whole process of motor calculations for given instance.
        :return:None
        """
        self.calc_construct_params()
        self.calc_stator_flux_dens()
        self.calc_stator_losses()
        self.calc_rotor_params()
        self.calc_rotor_flux_dens()
        self.calc_rotor_losses()

    def calc_construct_params(self):
        if self.limit != 0:
            self.kls = np.arange(-self.limit, self.limit + 1)
            self.klr = np.arange(-self.limit, self.limit + 1)
            self.gs = np.arange(-self.limit, self.limit + 1)
            self.gr = np.arange(-self.limit, self.limit + 1)
        else:
            self.kls = np.arange(-self.kls, self.kls + 1)
            self.klr = np.arange(-self.klr, self.klr + 1)
            self.gs = np.arange(-self.gs, self.gs + 1)
            self.gr = np.arange(-self.gr, self.gr + 1)

        self.q = self.m.Qs / (2 * self.m.m * self.m.p)
        self.ts = math.pi * self.m.ds / self.m.Qs
        self.tr = math.pi * self.m.dr / self.m.Qr
        self.taus = math.pi * self.m.ds / (2 * self.m.p)
        self.taur = math.pi * self.m.dr / (2 * self.m.p)
        self.cc = self.m.bss / self.ts + self.m.bsr / self.tr
        self.deltas = self.m.delta / self.cc * self.m.bss / self.ts
        self.gammas = (4 / math.pi) * ((self.m.bss / (2 * self.deltas)) * math.atan((self.m.bss / (2 * self.deltas)))
                                       - 0.5 * math.log(1 + (self.m.bss / (2 * self.deltas)) ** 2))

        self.kCs = self.ts / (self.ts - self.gammas * self.deltas)
        self.deltar = self.m.delta / self.cc * self.m.bsr / self.tr
        self.gammar = (4 / math.pi) * ((self.m.bsr / (2 * self.deltar)) * math.atan((self.m.bsr / (2 * self.deltar)))
                                       - 0.5 * math.log(1 + (self.m.bsr / (2 * self.deltar)) ** 2))

        self.kCr = self.tr / (self.tr - self.gammar * self.deltar)
        self.kC = self.kCs * self.kCr
        self.calculated_construct_params = True

    def print_construct_params(self):
        if self.calculated_construct_params:
            print("CONSTRUCTION PARAMETERS")
            print("*" * 50)
            print_var_value(self.kls, 'kls')
            print_var_value(self.klr, 'klr')
            print_var_value(self.gs, 'gs')
            print_var_value(self.gr, 'gr')
            print_var_value(self.q, 'q')
            print_var_value(self.ts, 'ts')
            print_var_value(self.tr, 'tr')
            print_var_value(self.taus, 'taus')
            print_var_value(self.taur, 'taur')
            print_var_value(self.cc, 'cc')
            print_var_value(self.deltas, 'deltas')
            print_var_value(self.gammas, 'gammas')
            print_var_value(self.kCs, 'kCs')
            print_var_value(self.deltar, 'deltar')
            print_var_value(self.gammar, 'gammar')
            print_var_value(self.kCr, 'kCr')
            print_var_value(self.kC, 'kC')
            print("*" * 50)
        else:
            print("PLEASE CALCULATE CONSTRUCTION PARAMETERS FIRST!")

    def calc_stator_flux_dens(self):

        self.vs = self.m.p * (6 * self.gs + 1)
        self.kCv = np.ones(self.vs.shape)

        for i, item in enumerate(self.vs):
            if abs(item) < (self.m.Qs - self.m.p):
                self.kCv[i] = self.kC

        if math.floor(self.q) == self.q:
            self.qc = self.m.Qs / (self.m.s * self.m.p)
        else:
            self.qc = 2 * self.q

        self.kqv = np.sin((self.vs / self.m.p) * (math.pi / 6)) / (
                self.qc * np.sin((self.vs / self.m.p) * (math.pi / (6 * self.qc))))
        self.tauQs = self.m.Qs / (2 * self.m.p)
        self.y = self.m.W / self.tauQs
        self.kyv = np.sin((self.vs / self.m.p) * self.y * (math.pi / 2))
        self.ksv = np.sin(self.vs * self.m.bss / self.m.ds) / (self.vs * self.m.bss / self.m.ds)
        self.kfv = self.kqv * self.kyv * self.ksv
        self.ky1 = np.sin((self.m.p / self.m.p) * self.y * (math.pi / 2))
        self.ks1 = np.sin(self.m.p * self.m.bss / self.m.ds) / (self.m.p * self.m.bss / self.m.ds)
        self.kq1 = np.sin((self.m.p / self.m.p) * (math.pi / 6)) / (
                self.qc * np.sin((self.m.p / self.m.p) * (math.pi / (6 * self.qc))))
        self.kfs = self.ky1 * self.ks1 * self.kq1
        self.Bfv = 1.7 * float(1e-3) * (self.m.N * self.kfv * self.m.Is) / (
                abs(self.vs) * self.m.delta * self.kCv * self.m.km)
        self.kls = self.kls[self.kls != 0]
        self.vls = self.kls * self.m.Qs + self.m.p
        self.x = 3 * self.q * self.kls * (1 - self.y) + self.kls + 1
        self.a = (-1) ** self.x
        self.ms = (self.m.bss / self.m.delta - 0.7) / 3.3
        self.beta = 0.43 * (1 - np.exp(-self.ms))
        self.kCs = self.ts / (self.ts - 1.6 * self.beta * self.m.bss)
        self.gammas = self.m.bss / self.m.ds
        self.Fks = 2 * np.sin(1.6 * np.abs(self.kls) * self.gammas * math.pi) / (
                math.pi * np.abs(self.kls) * (1 - (1.6 * self.kls * self.gammas) ** 2))
        self.Blk = self.a * (self.beta / 2) * self.kCs * self.Fks * self.m.Bdelta

        self.rzad_vs = np.hstack((self.vs, self.vls))
        self.sum_Bs = np.hstack((self.Bfv, np.abs(self.Blk)))
        # DUPLIKATY SUM_BS
        self.rzad_vs, self.sum_Bs = Utils.remove_flux_dens_duplicates_sin_fi(self.rzad_vs, self.sum_Bs, self.m.sinfi)
        self.vs = self.rzad_vs
        self.Bv = self.sum_Bs

        self.calculated_stator_fluxes = True

    def print_stator_flux_dens(self):
        if self.calculated_stator_fluxes:
            print("STATOR FLUX DENSITY")
            print("*" * 50)
            print_var_value(self.vs, 'vs')
            print_var_value(self.kCv, 'kCv')
            print_var_value(self.qc, 'qc')
            print_var_value(self.kqv, 'kqv')
            print_var_value(self.tauQs, 'tauQs')
            print_var_value(self.y, 'y')
            print_var_value(self.kyv, 'kyv')
            print_var_value(self.ksv, 'ksv')
            print_var_value(self.kfv, 'kfv')
            print_var_value(self.ky1, 'ky1')
            print_var_value(self.ks1, 'ks1')
            print_var_value(self.kq1, 'kq1')
            print_var_value(self.kfs, 'kfs')
            print_var_value(self.Bfv, 'Bfv')
            print_var_value(self.kls, 'kls')
            print_var_value(self.vls, 'vls')
            print_var_value(self.x, 'x')
            print_var_value(self.a, 'a')
            print_var_value(self.ms, 'ms')
            print_var_value(self.beta, 'beta')
            print_var_value(self.kCs, 'kCs')
            print_var_value(self.gammas, 'gammas')
            print_var_value(self.Fks, 'Fks')
            print_var_value(self.Blk, 'Blk')
            print_var_value(self.rzad_vs, 'rzad_vs')
            print_var_value(self.vls, 'vls')
            print("*" * 50)
        else:
            print("PLEASE CALCULATE STATOR FLUXES FIRST!")

    def calc_stator_losses(self):

        self.frv = self.m.fs * np.abs(1 - (self.vs / self.m.p) * (1 - self.m.s_p))
        self.Deltav = 1
        self.Bvs = self.Deltav * self.Bv
        self.Psv = ((self.m.roFe * float(1e3) * self.m.dr ** 2 * self.m.lFe * self.m.pCl * self.kCr) /
                    (2 * self.m.kFe * np.abs(self.vs))) * ((self.frv / 50) ** 2) * ((self.Bvs / 1.5) ** 2) * float(1e-9)
        self.Ps = np.sum(self.Psv)
        self.ks = 1 - 0.38 * (self.m.bsr / self.m.delta) ** (0.28)
        self.Bsv = self.Bvs * self.ks * self.kCr
        self.PAlv = (850 * self.Bsv ** 2 * self.frv ** 1.5 * self.m.bsr * (
                (math.pi * self.m.dr) / (2 * np.abs(self.vs))) * self.m.lFe *
                     self.m.Qr * self.kCr * float(1e-9))
        self.PAl = np.sum(self.PAlv)
        self.calculated_stator_losses = True

        self.PAl = np.around(self.PAl, 2)
        self.Ps = np.around(self.Ps, 2)

    def print_stator_losses(self):
        if self.calculated_stator_losses:
            print("CALCULATE STATOR LOSSES")
            print("*" * 50)
            print_var_value(self.frv, 'frv')
            print_var_value(self.Ps, 'Ps')
            print_var_value(self.PAl, 'PAl')
            print("*" * 50)
        else:
            print("PLEASE CALCULATE STATOR LOSSSES FIRST!")

    def calc_rotor_params(self):
        self.gr = self.gr[np.where(self.gr != 0)[0]]
        self.vrp = self.m.p + self.gr * self.m.Qr
        self.kCv = np.ones(self.vrp.shape)
        for i, item in enumerate(self.vrp):
            if abs(item) <= (self.m.Qr - self.m.p):
                self.kCv[i] = self.kCr

        self.ksvr = (np.sin(self.vrp * self.m.bsr / self.m.dr)) / (self.vrp * self.m.bsr / self.m.dr)
        self.ksr = np.sin(self.m.bsr / (2 * self.m.dr)) / (self.m.bsr / (2 * self.m.dr))
        self.bsq = self.tr
        self.alfasq = 2 * self.bsq * self.m.p / self.m.dr
        self.ksq = 2 * np.sin(self.alfasq / 2) / self.alfasq
        self.kfr = self.ksr * self.ksq
        self.Ir = np.sqrt(self.m.Isph ** 2 + self.m.I0ph ** 2 - 2 * self.m.I0ph * self.m.Isph * self.m.sinfi)
        self.Bfvp = ((np.sqrt(2) * self.m.m * self.m.mi0 * self.m.N * self.kfs * self.ksvr) / (
                math.pi * (self.m.delta / 1000) * self.kCv * np.abs(self.vrp) * self.m.km)) * self.Ir

        self.vrs = np.zeros(self.vs.size * self.gr.size)
        self.frs = np.zeros(self.vs.size * self.gr.size)
        for i, item in enumerate(self.vs):
            for j, gr_item in enumerate(self.gr):
                self.vrs[i * self.gr.size + j] = item + gr_item * self.m.Qr
                self.frs[i * self.gr.size + j] = self.m.fs * np.abs(
                    1 + (gr_item * self.m.Qr / self.m.p) * (1 - self.m.s_p))

        self.ksvr = (np.sin(self.vrs * self.m.bsr / self.m.dr)) / (self.vrs * self.m.bsr / self.m.dr)

        self.kCv = np.ones(self.vrs.size)
        for i, item in enumerate(self.vrs):
            if abs(item) < (self.m.Qr - self.m.p):
                self.kCv[i] = self.kCr

        self.alfaQv = 2 * math.pi * self.vs / self.m.Qr
        self.ktr = (self.tr - self.m.bsr) / self.tr
        self.Uicv = (np.sqrt(2) * math.pi ** 2 * self.frv * (self.m.lFe / 1000) *
                     ((self.m.dr / 1000) / self.m.Qr) * self.Bv * np.sin(self.vs * math.pi * self.ktr / self.m.Qr))

        self.gammar_teta = self.m.gammar_0 * (self.m.kgamma + 25) / (self.m.kgamma + self.m.tetar)
        self.Rc = (math.pi * self.m.dc / 1000) / (self.m.Qr * self.gammar_teta * self.m.sc)
        self.przekladnia = (2 * self.m.N * self.kfs / self.kfr) ** 2 * (3 / self.m.Qr)
        self.Rc = self.Rc * self.przekladnia
        self.kRv = 0.01 * self.m.h * np.sqrt(self.frv)
        self.Rpr = ((self.m.lpr / float(1e3)) / (self.gammar_teta * self.m.spr))
        self.Rpr = self.Rpr * self.przekladnia
        self.Rprv = self.Rpr * self.kRv
        self.Rcv = 2 * self.Rc + self.Rprv * (2 * np.sin(self.alfaQv / 2)) ** 2
        self.Ldeltac = (self.m.mi0 * (self.m.lFe / 1000) * ((self.tr - self.m.bsr) / 1000)) / (
                (self.m.delta / 1000) * self.kCs)
        self.kX = np.ones(self.frv.size)

        for i, value in enumerate(self.frv):
            if self.m.h >= (150 / np.sqrt(value)):
                self.kX[i] = 150 / (self.m.h * np.sqrt(value))

        self.frpodst = np.min(self.frv)
        self.Lqra01 = self.m.Xqra01 / (2 * math.pi * self.frpodst)
        self.Lqra01 = self.Lqra01 * self.przekladnia
        self.Lpr = self.m.Xpr / (2 * math.pi * self.frpodst)
        self.Lpr = self.Lpr * self.przekladnia
        self.LQrv = self.Lqra01 + self.Lpr * self.kX
        self.LQcv = self.LQrv * (2 * np.sin(self.alfaQv / 2)) ** 2
        self.Icv = self.Uicv / (np.sqrt(self.Rcv ** 2 + (2 * math.pi * self.frv * (self.LQcv + self.Ldeltac) ** 2)))
        self.Iprv = self.Icv * 2 * np.sin(self.alfaQv / 2)

        self.calculated_rotor_params = True

    def print_rotor_params(self):
        if self.calculated_rotor_params:
            print_var_value(self.gr, 'gr')
            print_var_value(self.vrp, 'vrp')
            print_var_value(self.kCv, 'kCv')
            print_var_value(self.ksvr, 'ksvr')
            print_var_value(self.ksr, 'ksr')
            print_var_value(self.bsq, 'bsq')
            print_var_value(self.alfasq, 'alfasq')
            print_var_value(self.ksq, 'ksq')
            print_var_value(self.kfr, 'kfr')
            print_var_value(self.Ir, 'Ir')
            print_var_value(self.Bfvp, 'Bfvp')
            print_var_value(self.vrs, 'vrs')
            print_var_value(self.frs, 'frs')
            print_var_value(self.kCv, 'kCv')
            print_var_value(self.ksvr, 'ksvr')
            print_var_value(self.alfaQv, 'alfaQv')
            print_var_value(self.ktr, 'ktr')
            print_var_value(self.Uicv, 'Uicv')
            print_var_value(self.gammar_teta, 'gammar_teta')
            print_var_value(self.Rc, 'Rc')
            print_var_value(self.przekladnia, 'przekladnia')
            print_var_value(self.Rc, 'Rc')
            print_var_value(self.kRv, 'kRv')
            print_var_value(self.Rpr, 'Rpr')
            print_var_value(self.Rpr, 'Rpr')
            print_var_value(self.Rprv, 'Rprv')
            print_var_value(self.Rcv, 'Rcv')
            print_var_value(self.Ldeltac, 'Ldeltac')
            print_var_value(self.kX, 'kX')
            print_var_value(self.frpodst, 'frpodst')
            print_var_value(self.Lqra01, 'Lqra01')
            print_var_value(self.Lqra01, 'Lqra01')
            print_var_value(self.Lpr, 'Lpr')
            print_var_value(self.LQrv, 'LQrv')
            print_var_value(self.LQcv, 'LQcv')
            print_var_value(self.Icv, 'Icv')
            print_var_value(self.Iprv, 'Iprv')
        else:
            print("CALCULATE ROTOR PARAMETERS FIRST!")

    def calc_rotor_flux_dens(self):
        gr_len = self.gr.size
        self.Bfvrs = np.zeros(self.vs.size * gr_len)
        for i, vs_item in enumerate(self.vs):
            for j, gr_item in enumerate(self.gr):
                indx = i * gr_len + j
                self.Bfvrs[indx] = ((self.m.mi0 * self.m.Qr * self.ksvr[indx]) / (np.sqrt(2) * math.pi *
                                                                                  (self.m.delta / 1000) * self.kCv[
                                                                                      indx] * np.abs(
                            self.vrs[indx]) * self.m.km)) * self.Iprv[i]

        self.klr = self.klr[np.where(self.klr != 0)]
        self.vrlp = self.m.p + self.klr * self.m.Qr
        self.gammasr = self.m.bsr / self.tr

        self.Fkr = (2 * np.sin(1.6 * np.abs(self.klr) * self.gammasr * math.pi)) / (math.pi * np.abs(self.klr)
                                                                                    * (1 - (
                        1.6 * np.abs(self.klr) * self.gammasr) ** 2))

        self.mr = (self.m.bsr / self.m.delta - 0.7) / 3.3
        self.betar = 0.43 * (1 - np.exp(-self.mr))

        self.Blkrp = (self.betar / 2) * self.kCr * self.Fkr * self.m.Bdelta
        self.vlrv = np.array([])

        for i, item in enumerate(self.vls):
            self.vlrv = np.hstack((self.vlrv, item + self.klr * self.m.Qr))

        self.epsilon = 3 * self.q * (1 - self.y)
        self.Blrs = np.array([])
        for i, item in enumerate(self.vls):
            self.B = self.Bvs[np.where(self.vs == self.vls[i])[0][0]]
            self.Blrs = np.hstack(
                (self.Blrs, (-1) ** (self.epsilon * self.kfs) * self.betar / 2 * self.kCr * self.Fkr * self.B))

        # USUWANIE DUPLIKATÓW

        # np.savez("fixtures/duplikaty_z_vrs, #" + str(limit), x=vrs, y=Bfvrs)
        self.vrs, self.Bfvrs = Utils.remove_flux_dens_duplicates(self.vrs, self.Bfvrs)
        # np.savez("fixtures/duplikaty_z_vrs_results, #" + str(limit), x=vrs, y=Bfvrs)

        self.suma_Bvr = self.Bfvrs
        self.rzad_vr = self.vrs
        self.suma_fr = self.frs

        # Sumowanie Bfvrs z Blrkp
        self.rzad_vr = np.hstack((self.rzad_vr, self.vrlp))
        self.suma_Bvr = np.hstack((self.suma_Bvr, self.Blkrp))

        # np.savez("fixtures/sumowanie_Bfvrs_z_Blkrp, #" + str(limit), x=rzad_vr, y=suma_Bvr)
        self.rzad_vr, self.suma_Bvr = Utils.remove_flux_dens_duplicates(self.rzad_vr, self.suma_Bvr)
        # np.savez("fixtures/sumowanie_Bfvrs_z_Blkrp_results, #" + str(limit), x=rzad_vr, y=suma_Bvr)

        # Sumowanie z Blrs

        self.rzad_vr = np.hstack((self.rzad_vr, self.vlrv))
        self.suma_Bvr = np.hstack((self.suma_Bvr, self.Blrs))

        # np.savez("fixtures/sumowanie_z_Blrs, #" + str(limit), x=rzad_vr, y=suma_Bvr)
        self.rzad_vr, self.suma_Bvr = Utils.remove_flux_dens_duplicates(self.rzad_vr, self.suma_Bvr)
        # np.savez("fixtures/sumowanie_z_Blrs_results, #" + str(limit), x=rzad_vr, y=suma_Bvr)

        self.rzad_vr = np.hstack((self.rzad_vr, self.vrp))
        self.suma_Bvr = np.hstack((self.suma_Bvr, self.Bfvp))
        # np.savez("fixtures/sumowanie_z_Bfvp, #" + str(limit), x=rzad_vr, y=suma_Bvr)

        self.rzad_vr, self.suma_Bvr = Utils.remove_flux_dens_duplicates_sqrt(self.rzad_vr, self.suma_Bvr)
        self.calculated_rotor_flux_dens = True

    def print_rotor_flux_dens(self):
        if self.calculated_rotor_flux_dens:
            print_var_value(self.rzad_vr, 'rzad_vr')
            print_var_value(self.suma_Bvr, 'suma_Bvr')
        else:
            print("PLEASE CALCULATE ROTOR FLUX DENSITIES FIRST!")

    def calc_rotor_losses(self):
        self.vr = self.rzad_vr
        self.Bvr = abs(self.suma_Bvr)
        self.fsv = self.m.fs * np.abs(1 + (self.vr / self.m.p) * (1 - self.m.s_p))
        self.Pssv = (((self.m.roFe * self.m.ds ** 2 * self.m.lFe * self.m.pCl * self.kCs * float(1e3)) / (
                2 * self.m.kFe * np.abs(self.vr))) * (self.fsv / 50) ** 2
                     * (self.Bvr / 1.5) ** 2 * float(1e-9))
        self.Pss = np.sum(self.Pssv)
        self.kts = (self.ts - self.m.bss) / self.ts
        self.etarv = np.sin(self.kts * self.vr * math.pi / self.m.Qs) / (self.kts * self.vr * math.pi / self.m.Qs)
        self.Btv = ((self.ts * self.kts * self.etarv) / (self.m.bts * self.m.kFe)) * self.Bvr
        self.p0 = 330
        self.pk = 540
        self.Bk = 1.35
        self.sigmak = 4
        self.kappa = 1.55
        self.xp = (self.Btv / self.Bk) ** self.sigmak
        self.ppv = (self.p0 + (self.pk - self.p0) * (1 - np.exp(-self.xp))) * (self.fsv / 1000) ** self.kappa
        self.Ppv = self.m.mts * self.Btv ** 2 * self.ppv
        self.Pp = sum(self.Ppv)
        self.calculated_rotor_losses = True

        self.Pss = np.around(self.Pss, 2)
        self.Pp = np.around(self.Pp, 2)

    def print_rotor_losses(self):
        if self.calculated_rotor_losses:
            print(f"Straty dodatkowe w zebach wirnika Ps = {self.Ps:10}")
            print(f"Straty dodatkowe w klatce wirnika PAl = {self.PAl:10}")
            print(f"Straty powierzchniowe w zebach stojana Pss = {self.Pss:10}")
            print(f"Straty pulsacyjne w zebach stojana Pp = {self.Pp:10}")
        else:
            print("CALCULATE ROTOR LOSSES FIRST!")

    def get_motor_losses(self) -> tuple:
        if self.calculated_stator_losses and self.calculated_rotor_losses:
            return self.Ps, self.PAl, self.Pss, self.Pp
        else:
            raise Exception("Calculate stator and rotor losses first!")

    def stator_fluxes(self):
        if self.calculated_stator_fluxes:
            fluxes = FluxDensity(self.vs, self.Bv)
            fluxes.sort()
            return fluxes
        else:
            return None

    def rotor_fluxes(self):
        if self.calculated_rotor_flux_dens:
            fluxes = FluxDensity(self.rzad_vr, self.suma_Bvr)
            fluxes.sort()
            return fluxes
        else:
            return None

    def stator_losses(self):
        if self.calculated_stator_losses:
            losses_psv = Losses(self.vs, self.Psv)
            losses_palv = Losses(self.vs, self.PAlv)
            losses_psv.sort()
            losses_palv.sort()
            return losses_psv, losses_palv
        else:
            return None

    def rotor_losses(self):
        if self.calculated_rotor_losses:
            losses_pssv = Losses(self.vr, self.Pssv)
            losses_ppv = Losses(self.vr, self.Ppv)
            losses_pssv.sort()
            losses_ppv.sort()
            return losses_pssv, losses_ppv
        else:
            return None

    def stator_losses_serializable(self):
        losses_psv, losses_palv = self.stator_losses()
        return {"vs": losses_psv.order, "psv": losses_psv.losses, "palv": losses_palv.losses}

    def rotor_losses_serializable(self):
        losses_pssv, losses_ppv = self.rotor_losses()
        return {"vr": losses_pssv.order, "pssv": losses_pssv.losses, "ppv": losses_ppv.losses}

    def __str__(self):
        txt = ""
        pl_eng_dict = {True: "Tak", False: "Nie"}
        txt += f"Limit = {self.limit}\n"
        txt += f"Obliczono parametry konstrukcyjne".ljust(45) + f" = {pl_eng_dict[self.calculated_construct_params]}\n"
        txt += f"Obliczono indukcjne stojana".ljust(45) + f" = {pl_eng_dict[self.calculated_stator_fluxes]}\n"
        txt += f"Obliczono straty stojana".ljust(45) + f" = {pl_eng_dict[self.calculated_stator_losses]}\n"
        txt += f"Obliczono parametry wirnika".ljust(45) + f" = {pl_eng_dict[self.calculated_rotor_params]}\n"
        txt += f"Obliczono indukcje wirnika".ljust(45) + f" = {pl_eng_dict[self.calculated_rotor_flux_dens]}\n"
        txt += f"Obliczono straty wirnika".ljust(45) + f" = {pl_eng_dict[self.calculated_rotor_losses]}\n"

        if (self.calculated_construct_params and self.calculated_stator_fluxes and self.calculated_stator_losses and
                self.calculated_rotor_params and self.calculated_rotor_flux_dens and self.calculated_rotor_losses):
            txt += f"Straty dodatkowe w zebach wirnika Ps".ljust(45) + f" = {self.Ps:10}\n"
            txt += f"Straty dodatkowe w klatce wirnika PAl".ljust(45) + f" = {self.PAl:10}\n"
            txt += f"Straty powierzchniowe w zebach stojana Pss".ljust(45) + f" = {self.Pss:10}\n"
            txt += f"Straty pulsacyjne w zebach stojana Pp".ljust(45) + f" = {self.Pp:10}\n"
        else:
            txt += "OBLICZENIA NIE ZOSTAŁY WYKONANE CAŁOWICIE"
        return txt


if __name__ == "__main__":
    motor = Motor()
    motorCalc = MotorCalc(motor, limit=5)
    motorCalc.calc_construct_params()
    motorCalc.calc_stator_flux_dens()
    motorCalc.print_stator_flux_dens()
    motorCalc.calc_stator_losses()
    motorCalc.print_stator_losses()
    motorCalc.calc_rotor_params()
    motorCalc.print_rotor_params()
    motorCalc.calc_rotor_flux_dens()
    motorCalc.print_rotor_flux_dens()
    motorCalc.calc_rotor_losses()
    motorCalc.print_rotor_losses()

    print("*" * 50)
    print(motorCalc.stator_losses()[0])
    print(motorCalc.stator_losses()[1])
    print("*" * 50)
    print(motorCalc.rotor_losses()[0])
    print(motorCalc.rotor_losses()[1])
    from collections import namedtuple
