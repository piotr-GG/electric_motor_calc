import math
import numpy as np
import sys

from utils import Utils


# TODO: MOVE TO UTILS
def print_var_value(var, name: str):
    print(f"{name} = {var}")


# TODO: SPLIT INTO SEVERAL SMALLER FUNCTIONS

save_to_file = False


class MotorCalc:
    def __init__(self):


p = 2  # Liczba par biegunów [-]
Qs = 36  # Liczba żłobków stojana [-]
Qr = 28  # Liczba żłobków wirnika [-]
W = 9  # Liczba żłobków oddzielająca od siebie prawy i lewy bok zezwoju [-]
bss = 3.6  # Szerokość szczerbiny żłobka stojana [mm]
bsr = 1  # Szerokość szczerbiny żłobka wirnika [mm]
bts = 9.83  # Szerokosc zeba stojana [mm]
btr = 16.18  # Szerokosc zeba wirnika [mm]
delta = 0.45  # Szerokość szczeliny powietrznej [mm]
N = 141  # Liczba zwojów uzwojenia [-]
m = 3  # Liczba pasm uzwojenia [-]
ds = 154  # Szerokość zewnętrzna stojana [mm]
dr = ds - 2 * delta  # Szerokość zewnętrzna wirnika [mm]
s = 6  # Liczba stref boków uzwojenia na parę biegunów / stref pasmowych na przestrzeni pary biegunów [-]
Bdelta = 0.7424  # Indukcja w szczelinie powietrznej [T]
mi0 = 1.257 * 10 ** -6  # Przenikalnosc magnetyczna prozni
cosfi = 0.84  # Wspolczynnik mocy [-]
sinfi = math.sqrt(1 - cosfi ** 2)  # Sinus fi [-]
s_p = 0.01937  # Poślizg [-]
fs = 50  # Częstotliwośc napiecia zasilajacego [Hz]
roFe = 7.8  # Gęstosc (masa wlasciwa) materialu rdzenia [kg/dm3]
lFe = 199  # Dlugosc pakietu silnika [mm]
pCl = 4.5  # Gestosc strat z pradow wirowych przy 50Hz i 1,5 T [W/kg]
kFe = 0.96  # Wspolczynnik zapelnienia zelaza [-]
lpr = 190  # Dlugosc preta [mm]
spr = 165  # Przekroj preta [mm^2]
h = 37  # Wysokosc preta [mm]
Rc = 1000  # Rezystancja klatki [Ohm]
ks = 1  # Wspolczynnik szczerbiny wynikajacy z rozkladu okladu pradowego na szerokosci szczerbiny [-]
mts = 9.18  # Masa zebow stojana [kg]
Is = 28.66  # Prąd przewodowy pobierany z sieci [A]
I0 = 13.09  # Prad przewodowy biegu jalowego [A]
Isph = Is / math.sqrt(3)  # Prąd fazowy pobierany z sieci [A]
I0ph = I0 / math.sqrt(3)  # Prad fazowy biegu jalowego [A]
Ipr = 411  # Prąd w pręcie klatki wirnika [A]
Vp = 374.9  # Napiecie magnetyczne w szczelinie [A]
Vsd = 50.57  # Napiecie magnetyczne w zebach [A]
km = 1 + Vsd / Vp  # Współczynnik nasycenia obwodu magnetycznego [-]
gammar_0 = 35  # przewodnosc cieplna materialu preta klatki wirnika w temperaturze 20 deg C [Sm / mm^2]
tetar = 135  # Temperatura uzwojenia wirnika przyjeta do obliczen [deg C]
kgamma = 225  # Wspolczynnik do obliczenia przewodnosci cieplnej w temperaturze tetar [-]
dc = 110  # Srednica pierscienia zwierajacego klatke wirnika [mm]
sc = 800  # Przekroj pierscienia zwierajacego klatke wirnika [mm2]

Xqra01 = 5.9276e-05  # Reaktancja niepodlegajaca wypieraniu pradu, niesprowadzona
Xpr = 0.00017001  # Reaktancja podlegajaca wypieraniu pradu, sprowadzona

pi = math.pi
limit = 5

if __name__ == "__main__":

    load_input_vals()
    kls = np.arange(-limit, limit + 1)
    klr = np.arange(-limit, limit + 1)
    gs = np.arange(-limit, limit + 1)
    gr = np.arange(-limit, limit + 1)

    print_var_value(kls, 'kls')
    print_var_value(klr, 'klr')
    print_var_value(gs, 'gs')
    print_var_value(gr, 'gr')

    print("*" * 50)
    q = Qs / (2 * m * p)
    print(q / 2.3)
    print_var_value(q, 'q')
    ts = pi * ds / Qs
    print_var_value(ts, 'ts')
    tr = pi * dr / Qr
    print_var_value(tr, 'tr')
    taus = pi * ds / (2 * p)
    print_var_value(taus, 'taus')
    taur = pi * dr / (2 * p)
    print_var_value(taur, 'taur')
    cc = bss / ts + bsr / tr
    print_var_value(cc, 'cc')
    deltas = delta / cc * bss / ts
    print_var_value(deltas, 'deltas')
    gammas = (4 / pi) * ((bss / (2 * deltas)) * math.atan((bss / (2 * deltas)))
                         - 0.5 * math.log(1 + (bss / (2 * deltas)) ** 2))
    print_var_value(gammas, 'gammas')
    kCs = ts / (ts - gammas * deltas)
    print_var_value(kCs, 'kCs')
    deltar = delta / cc * bsr / tr
    print_var_value(deltar, 'deltar')
    gammar = (4 / pi) * ((bsr / (2 * deltar)) * math.atan((bsr / (2 * deltar)))
                         - 0.5 * math.log(1 + (bsr / (2 * deltar)) ** 2))
    print_var_value(gammar, 'gammar')
    kCr = tr / (tr - gammar * deltar)
    print_var_value(kCr, 'kCr')
    kC = kCs * kCr
    print_var_value(kC, 'kC')

    vs = p * (6 * gs + 1)
    print(vs)
    kCv = np.ones(vs.shape)
    print(kCv)
    for i, item in enumerate(vs):
        if abs(item) < (Qs - p):
            kCv[i] = kC
    print(kCv)

    if math.floor(q) == q:
        qc = Qs / (s * p)
    else:
        qc = 2 * q
    print_var_value(qc, 'qc')

    kqv = np.sin((vs / p) * (pi / 6)) / (qc * np.sin((vs / p) * (pi / (6 * qc))))
    print(kqv)
    tauQs = Qs / (2 * p)
    print_var_value(tauQs, 'tauQs')
    y = W / tauQs
    print_var_value(y, 'y')
    kyv = np.sin((vs / p) * y * (pi / 2))
    print_var_value(kyv, 'kyv')
    ksv = np.sin(vs * bss / ds) / (vs * bss / ds)
    print_var_value(ksv, 'ksv')
    kfv = kqv * kyv * ksv
    print_var_value(kfv, 'kfv')
    ky1 = np.sin((p / p) * y * (pi / 2))
    print_var_value(ky1, 'ky1')
    ks1 = np.sin(p * bss / ds) / (p * bss / ds)
    print_var_value(ks1, 'ks1')
    kq1 = np.sin((p / p) * (pi / 6)) / (qc * np.sin((p / p) * (pi / (6 * qc))))
    print_var_value(kq1, 'kq1')
    kfs = ky1 * ks1 * kq1
    print_var_value(kfs, 'kfs')
    Bfv = 1.7 * float(1e-3) * (N * kfv * Is) / (abs(vs) * delta * kCv * km)
    print_var_value(Bfv, 'Bfv')
    kls = kls[kls != 0]
    print_var_value(kls, 'kls')
    vls = kls * Qs + p
    print_var_value(vls, 'vls')
    x = 3 * q * kls * (1 - y) + kls + 1
    print_var_value(x, 'x')
    a = (-1) ** x
    print_var_value(a, 'a')
    ms = (bss / delta - 0.7) / 3.3
    print_var_value(ms, 'ms')
    beta = 0.43 * (1 - np.exp(-ms))
    print_var_value(beta, 'beta')
    kCs = ts / (ts - 1.6 * beta * bss)
    print_var_value(kCs, 'kCs')
    gammas = bss / ds
    print_var_value(gammas, 'gammas')
    Fks = 2 * np.sin(1.6 * np.abs(kls) * gammas * pi) / (pi * np.abs(kls) * (1 - (1.6 * kls * gammas) ** 2))
    print_var_value(Fks, 'Fks')
    Blk = a * (beta / 2) * kCs * Fks * Bdelta
    print_var_value(Blk, 'Blk')

    sum_Bs = Bfv
    rzad_vs = vs

    print_var_value(rzad_vs, 'rzad_vs')
    print_var_value(vls, 'vls')

    rzad_vs = np.hstack((vs, vls))
    sum_Bs = np.hstack((Bfv, np.abs(Blk)))

    print('*' * 50)
    print_var_value(rzad_vs, 'rzad_vs')
    print_var_value(sum_Bs, 'sum_Bs')

    i = 0
    print(rzad_vs)
    print(sum_Bs)

    # DUPLIKATY SUM_BS
    # np.savez("fixtures/duplikaty_sum_Bs, #" + str(limit), x=rzad_vs, y=sum_Bs)

    rzad_vs, sum_Bs = Utils.remove_flux_dens_duplicates_sin_fi(rzad_vs, sum_Bs, sinfi)

    print(rzad_vs, 'rzad_vs')
    print(sum_Bs, 'sum_Bs')

    # np.savez("fixtures/duplikaty_sum_Bs_results, #" + str(limit), x=rzad_vs, y=sum_Bs)

    vs = rzad_vs
    Bv = sum_Bs

    frv = fs * np.abs(1 - (vs / p) * (1 - s_p))
    print_var_value(frv, 'frv')
    Deltav = 1
    Bvs = Deltav * Bv

    Psv = ((roFe * float(1e3) * dr ** 2 * lFe * pCl * kCr) /
           (2 * kFe * np.abs(vs))) * ((frv / 50) ** 2) * ((Bvs / 1.5) ** 2) * float(1e-9)
    Ps = np.sum(Psv)
    print_var_value(Ps, 'Ps')

    ks = 1 - 0.38 * (bsr / delta) ** (0.28)
    Bsv = Bvs * ks * kCr
    PAlv = (850 * Bsv ** 2 * frv ** 1.5 * bsr * ((pi * dr) / (2 * np.abs(vs))) * lFe *
            Qr * kCr * float(1e-9))
    PAl = np.sum(PAlv)
    print_var_value(PAl, 'PAl')

    #
    #
    #
    #
    #  WIRNIK
    #
    #
    #
    #

    print("*" * 50)
    print("*" * 20, "WIRNIK".center(10), "*" * 20)
    print("*" * 50)

    gr = gr[np.where(gr != 0)[0]]
    print_var_value(gr, 'gr')

    vrp = p + gr * Qr
    print_var_value(vrp, 'vrp')
    kCv = np.ones(vrp.shape)
    for i, item in enumerate(vrp):
        if abs(item) <= (Qr - p):
            kCv[i] = kCr
    print_var_value(kCv, 'kCv')

    ksvr = (np.sin(vrp * bsr / dr)) / (vrp * bsr / dr)
    print_var_value(ksvr, 'ksvr')
    ksr = np.sin(bsr / (2 * dr)) / (bsr / (2 * dr))
    print_var_value(ksr, 'ksr')
    bsq = tr
    print_var_value(bsq, 'bsq')
    alfasq = 2 * bsq * p / dr
    print_var_value(alfasq, 'alfasq')
    ksq = 2 * np.sin(alfasq / 2) / alfasq
    print_var_value(ksq, 'ksq')
    kfr = ksr * ksq
    print_var_value(kfr, 'kfr')
    Ir = np.sqrt(Isph ** 2 + I0ph ** 2 - 2 * I0ph * Isph * sinfi)
    print_var_value(Ir, 'Ir')
    Bfvp = ((np.sqrt(2) * m * mi0 * N * kfs * ksvr) / (
            pi * (delta / 1000) * kCv * np.abs(vrp) * km)) * Ir
    print_var_value(Bfvp, 'Bfvp')

    vrs = np.zeros(vs.size * gr.size)
    frs = np.zeros(vs.size * gr.size)
    for i, item in enumerate(vs):
        for j, gr_item in enumerate(gr):
            vrs[i * gr.size + j] = item + gr_item * Qr
            frs[i * gr.size + j] = fs * np.abs(1 + (gr_item * Qr / p) * (1 - s_p))

    print_var_value(vrs, 'vrs')
    print_var_value(frs, 'frs')

    ksvr = (np.sin(vrs * bsr / dr)) / (vrs * bsr / dr)
    print_var_value(ksvr, 'ksvr')

    kCv = np.ones(vrs.size)
    for i, item in enumerate(vrs):
        if abs(item) < (Qr - p):
            kCv[i] = kCr
    print_var_value(kCv, 'kCv')

    alfaQv = 2 * pi * vs / Qr
    print_var_value(alfaQv, 'alfaQv')
    ktr = (tr - bsr) / tr
    print_var_value(ktr, 'ktr')

    Uicv = (np.sqrt(2) * pi ** 2 * frv * (lFe / 1000) *
            ((dr / 1000) / Qr) * Bv * np.sin(vs * pi * ktr / Qr))
    print_var_value(Uicv, 'Uicv')

    gammar_teta = gammar_0 * (kgamma + 25) / (kgamma + tetar)
    print_var_value(gammar_teta, 'gammar_teta')

    Rc = (pi * dc / 1000) / (Qr * gammar_teta * sc)
    print_var_value(Rc, 'Rc')

    przekladnia = (2 * N * kfs / kfr) ** 2 * (3 / Qr)
    print_var_value(przekladnia, 'przekladnia')

    Rc = Rc * przekladnia
    print_var_value(Rc, 'Rc')

    kRv = 0.01 * h * np.sqrt(frv)
    print_var_value(kRv, 'kRv')
    Rpr = ((lpr / float(1e3)) / (gammar_teta * spr))
    print_var_value(Rpr, 'Rpr')
    Rpr = Rpr * przekladnia
    print_var_value(Rpr, 'Rpr')
    Rprv = Rpr * kRv
    print_var_value(Rprv, 'Rprv')
    Rcv = 2 * Rc + Rprv * (2 * np.sin(alfaQv / 2)) ** 2
    print_var_value(Rcv, 'Rcv')
    Ldeltac = (mi0 * (lFe / 1000) * ((tr - bsr) / 1000)) / ((delta / 1000) * kCs)
    print_var_value(Ldeltac, 'Ldeltac')
    kX = np.ones(frv.size)

    for i, value in enumerate(frv):
        if h >= (150 / np.sqrt(value)):
            kX[i] = 150 / (h * np.sqrt(value))

    print_var_value(kX, 'kX')

    frpodst = np.min(frv)
    print_var_value(frpodst, 'frpodst')
    Lqra01 = Xqra01 / (2 * pi * frpodst)
    print_var_value(Lqra01, 'Lqra01')
    Lqra01 = Lqra01 * przekladnia
    print_var_value(Lqra01, 'Lqra01')
    Lpr = Xpr / (2 * pi * frpodst)
    print_var_value(Lpr, 'Lpr')
    Lpr = Lpr * przekladnia
    print_var_value(Lpr, 'Lpr')
    LQrv = Lqra01 + Lpr * kX
    print_var_value(LQrv, 'LQrv')
    LQcv = LQrv * (2 * np.sin(alfaQv / 2)) ** 2
    print_var_value(LQcv, 'LQcv')
    Icv = Uicv / (np.sqrt(Rcv ** 2 + (2 * pi * frv * (LQcv + Ldeltac) ** 2)))
    print_var_value(Icv, 'Icv')
    Iprv = Icv * 2 * np.sin(alfaQv / 2)
    print_var_value(Iprv, 'Iprv')

    gr_len = gr.size
    Bfvrs = np.zeros(vs.size * gr_len)
    for i, vs_item in enumerate(vs):
        for j, gr_item in enumerate(gr):
            indx = i * gr_len + j
            Bfvrs[indx] = ((mi0 * Qr * ksvr[indx]) / (np.sqrt(2) * pi *
                                                      (delta / 1000) * kCv[indx] * np.abs(vrs[indx]) * km)) * Iprv[i]

    print_var_value(vrs, 'vrs')
    print_var_value(Bfvrs, 'Bfvrs')

    klr = klr[np.where(klr != 0)]
    print_var_value(klr, 'klr')

    vrlp = p + klr * Qr
    print_var_value(vrlp, 'vrlp')
    gammasr = bsr / tr
    print_var_value(gammasr, 'gammasr')

    Fkr = (2 * np.sin(1.6 * np.abs(klr) * gammasr * pi)) / (pi * np.abs(klr)
                                                            * (1 - (1.6 * np.abs(klr) * gammasr) ** 2))
    print_var_value(Fkr, 'Fkr')

    mr = (bsr / delta - 0.7) / 3.3
    print_var_value(mr, 'mr')
    betar = 0.43 * (1 - np.exp(-mr))
    print_var_value(betar, 'betar')

    Blkrp = (betar / 2) * kCr * Fkr * Bdelta

    print_var_value(vrlp, 'vrlp')
    print_var_value(Blkrp, 'Blrkp')

    vlrv = np.array([])

    for i, item in enumerate(vls):
        vlrv = np.hstack((vlrv, item + klr * Qr))
    print_var_value(vlrv, 'vlrv')

    epsilon = 3 * q * (1 - y)
    print_var_value(epsilon, 'epsilon')

    Blrs = np.array([])
    for i, item in enumerate(vls):
        B = Bvs[np.where(vs == vls[i])[0][0]]
        Blrs = np.hstack((Blrs, (-1) ** (epsilon * kfs) * betar / 2 * kCr * Fkr * B))
    print_var_value(Blrs, 'Blrs')

    # USUWANIE DUPLIKATÓW

    print("*" * 50)
    print("USUWANIE DUPLIKATÓW Z vrs".center(50))
    print("*" * 50)

    print("vrs.size = {0}".format(vrs.size))
    print("Bfvrs.size = {0}".format(Bfvrs.size))

    print("*" * 50)
    print("PRZED USUNIECIEM")
    print_var_value(vrs, 'vrs')
    print_var_value(Bfvrs, 'Bfvrs')

    # np.savez("fixtures/duplikaty_z_vrs, #" + str(limit), x=vrs, y=Bfvrs)

    i = 0

    vrs, Bfvrs = Utils.remove_flux_dens_duplicates(vrs, Bfvrs)

    print("*" * 50)
    print("PO USUNIECIU")
    print_var_value(vrs, 'vrs')
    print_var_value(Bfvrs, 'Bfvrs')
    # np.savez("fixtures/duplikaty_z_vrs_results, #" + str(limit), x=vrs, y=Bfvrs)

    print("vrs.size = {0}".format(vrs.size))
    print("Bfvrs.size = {0}".format(Bfvrs.size))

    suma_Bvr = Bfvrs
    rzad_vr = vrs
    suma_fr = frs

    # Sumowanie Bfvrs z Blrkp
    rzad_vr = np.hstack((rzad_vr, vrlp))
    suma_Bvr = np.hstack((suma_Bvr, Blkrp))

    print("*" * 50)
    print("SUMOWANIE Bfvrs z Blrkp")
    print("*" * 50)

    # np.savez("fixtures/sumowanie_Bfvrs_z_Blkrp, #" + str(limit), x=rzad_vr, y=suma_Bvr)

    print("PRZED USUNIECIEM:")
    print_var_value(rzad_vr.size, 'rzad_vr.size')
    print_var_value(suma_Bvr.size, 'suma_Bvr.size')

    rzad_vr, suma_Bvr = Utils.remove_flux_dens_duplicates(rzad_vr, suma_Bvr)

    print("PO USUNIECIU:")
    # np.savez("fixtures/sumowanie_Bfvrs_z_Blkrp_results, #" + str(limit), x=rzad_vr, y=suma_Bvr)

    print_var_value(rzad_vr, 'rzad_vr')
    print_var_value(suma_Bvr, 'suma_Bvr')

    print_var_value(rzad_vr.size, 'rzad_vr.size')
    print_var_value(suma_Bvr.size, 'suma_Bvr.size')

    # Sumowanie z Blrs

    rzad_vr = np.hstack((rzad_vr, vlrv))
    suma_Bvr = np.hstack((suma_Bvr, Blrs))

    # np.savez("fixtures/sumowanie_z_Blrs, #" + str(limit), x=rzad_vr, y=suma_Bvr)

    print("*" * 50)
    print("SUMOWANIE Z Blrs")
    print("Rzad vr przed usunieciem duplikatow:", rzad_vr.size)
    print("Suma Bvr przed usunieciem duplikatow:", suma_Bvr.size)

    rzad_vr, suma_Bvr = Utils.remove_flux_dens_duplicates(rzad_vr, suma_Bvr)

    print("Rzad vr po usunieciu duplikatow:", rzad_vr.size)
    print("Suma Bvr po usunieciu duplikatow:", suma_Bvr.size)

    # np.savez("fixtures/sumowanie_z_Blrs_results, #" + str(limit), x=rzad_vr, y=suma_Bvr)

    print("PO DODANIU Blrs")

    print_var_value(rzad_vr, 'rzad_vr')
    print_var_value(suma_Bvr, 'suma_Bvr')

    print("*" * 50)
    print("SUMOWANIE Z Bfvp")
    rzad_vr = np.hstack((rzad_vr, vrp))
    suma_Bvr = np.hstack((suma_Bvr, Bfvp))

    # np.savez("fixtures/sumowanie_z_Bfvp, #" + str(limit), x=rzad_vr, y=suma_Bvr)

    print("Rzad vr przed usunieciem duplikatow:", rzad_vr.size)
    print("Suma Bvr przed usunieciem duplikatow:", suma_Bvr.size)

    rzad_vr, suma_Bvr = Utils.remove_flux_dens_duplicates_sqrt(rzad_vr, suma_Bvr)

    print("Rzad vr po usunieciu duplikatow:", rzad_vr.size)
    print("Suma Bvr po usunieciu duplikatow:", suma_Bvr.size)

    # np.savez("fixtures/sumowanie_z_Bfvp_results, #" + str(limit), x=rzad_vr, y=suma_Bvr)

    # STRATY W STOJANIE

    vr = rzad_vr
    Bvr = abs(suma_Bvr)

    fsv = fs * np.abs(1 + (vr / p) * (1 - s_p))

    Pssv = (((roFe * ds ** 2 * lFe * pCl * kCs * float(1e3)) / (2 * kFe * np.abs(vr))) * (fsv / 50) ** 2
            * (Bvr / 1.5) ** 2 * float(1e-9))
    Pss = np.sum(Pssv)
    print_var_value(Pss, 'Pss')

    kts = (ts - bss) / ts
    etarv = np.sin(kts * vr * pi / Qs) / (kts * vr * pi / Qs)
    Btv = ((ts * kts * etarv) / (bts * kFe)) * Bvr
    p0 = 330
    pk = 540
    Bk = 1.35
    sigmak = 4
    kappa = 1.55

    xp = (Btv / Bk) ** sigmak
    ppv = (p0 + (pk - p0) * (1 - np.exp(-xp))) * (fsv / 1000) ** kappa
    Ppv = mts * Btv ** 2 * ppv
    Pp = sum(Ppv)

    print("STRATY KOŃCOWE: ")
    print(f"Straty dodatkowe w zebach wirnika Ps = {Ps:10}")
    print(f"Straty dodatkowe w klatce wirnika PAl = {PAl:10}")
    print(f"Straty powierzchniowe w zebach stojana Pss = {Pss:10}")
    print(f"Straty pulsacyjne w zebach stojana Pp = {Pp:10}")


