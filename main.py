import math
import numpy as np
import sys


# from decimal import *


def print_var_value(var, name: str):
    print(f"{name} = {var}")


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
kls = np.arange(-limit, limit + 1)
klr = np.arange(-limit, limit + 1)
gs = np.arange(-limit, limit + 1)
gr = np.arange(-limit, limit + 1)

print_var_value(kls, 'kls')
print_var_value(klr, 'klr')
print_var_value(gs, 'gs')
print_var_value(gr, 'gr')

# getcontext().prec = 3
print('*' * 50)
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
                     - 0.5 * math.log(1 + ((bss / (2 * deltas))) ** 2))
print_var_value(gammas, 'gammas')
kCs = ts / (ts - gammas * deltas)
print_var_value(kCs, 'kCs')
deltar = delta / cc * bsr / tr
print_var_value(deltar, 'deltar')
gammar = (4 / pi) * ((bsr / (2 * deltar)) * math.atan((bsr / (2 * deltar)))
                     - 0.5 * math.log(1 + ((bsr / (2 * deltar))) ** 2))
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
# test = [x for x in vs if abs(x) < (Qs-p)]
# print(test)
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
kyv = np.sin((vs / p)) * y * pi / 2
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

# for i, item in enumerate(rzad_vs):
#     x = np.where(vls == item)[0]
#     if x.size != 0:
#         vls_ind = x[0]
#         print(vls_ind, " : ", vls[vls_ind])
#         sum_Bs[i] = np.sqrt(sum_Bs[i]**2 + Blk[vls_ind]**2 +
#                             2 * sum_Bs[i] * Blk[vls_ind]*sinfi)
#
# vls_not_in_rzad_vs = np.where(vls == rzad_vs)
# print(vls_not_in_rzad_vs)

rzad_vs = np.hstack((vs, vls))
sum_Bs = np.hstack((Bfv, Blk))

print('*' * 50)
print_var_value(rzad_vs, 'rzad_vs')
print_var_value(sum_Bs, 'sum_Bs')

# unique_vals_vs = np.array([])
# unique_vals_Bs = np.array([])

# zrobić to whilem, zrobić kopię arraya i z niej usuwac, a reszte dodawac do jakiejs zmiennej typu temp
# robic tak az do konca arraya
# dodawac duplikaty
# za pomocą tego polecenia trzeba w while usuwac indeksy z kopii
# rzad_vs = rzad_vs[np.where(rzad_vs != -34)[0]]
# temp_Bs = np.array([])
# temp_vs = np.copy(rzad_vs)
# new_vs = np.array([])
# i = 0


i = 0

# rzad_vs = np.array([3,5,7,8,12,3,5,3,2,3,1,18,18])
# sum_Bs = np.array([1,1,1,1,1,1,1,1,1,1,1,1,1])

print(rzad_vs)
print(sum_Bs)
while i < rzad_vs.size:
    indices = np.where(rzad_vs[i] == rzad_vs)[0]
    idx_to_del = indices[1:]
    if indices.size == 2:
        Bs1, Bs2 = sum_Bs[i], sum_Bs[idx_to_del[0]]
        sum_Bs[i] = np.sqrt(Bs1 ** 2 + Bs2 ** 2 + 2 * Bs1 * Bs2 * sinfi)
    else:
        for j in idx_to_del:
            sum_Bs[i] = sum_Bs[i] + sum_Bs[j]
    rzad_vs = np.delete(rzad_vs, idx_to_del)
    sum_Bs = np.delete(sum_Bs, idx_to_del)
    i += 1

print(rzad_vs)
print(sum_Bs)

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

gr = gr[np.where(gr != 0)[0]]
print_var_value(gr, 'gr')

vrp = p + gr * Qr
kCv = np.ones(vrp.shape)
for i, item in enumerate(vrp):
    if abs(item) < (Qr - p):
        kCv[i] = kC
print(kCv)

ksvr = (np.sin(vrp * bsr / dr)) / (vrp * bsr / dr)
ksr = np.sin(bsr / (2 * dr)) / (bsr / (2 * dr))
bsq = tr
alfasq = 2 * bsq * p / dr
ksq = 2 * np.sin(alfasq / 2) / alfasq
kfr = ksr * ksq
Ir = np.sqrt(Isph ** 2 + I0ph ** 2 - 2 * I0ph * Isph * sinfi)

Bfvp = ((np.sqrt(2) * m * mi0 * N * kfs * ksvr) / (
        pi * (delta / 1000) * kCv * np.abs(vrp) * km)) * Ir

vrs = np.zeros(vs.size * gr.size)
frs = np.zeros(vs.size * gr.size)
for i, item in enumerate(vs):
    for j, gr_item in enumerate(gr):
        vrs[i * gr.size + j] = item + gr_item * Qr
        frs[i * gr.size + j] = fs * np.abs(1 + (gr_item * Qr / p) * (1 - s_p))

print(vrs)
print(frs)

ksvr = (np.sin(vrs * bsr / dr)) / (vrs * bsr / dr)
kCv = np.ones(vrs.size)
for i, item in enumerate(vrs):
    if abs(item) < (Qr - p):
        kCv[i] = kCr
print(kCv)

alfaQv = 2 * pi * vs / Qr
ktr = (tr - bsr) / tr

Uicv = (np.sqrt(2) * pi ** 2 * frv * (lFe / 1000) *
        ((dr / 1000) / Qr) * Bv * np.sin(vs * pi * ktr / Qr))

gammar_teta = gammar_0 * (kgamma + 25) / (kgamma + tetar)
Rc = (pi * dc / 1000) / (Qr * gammar_teta * sc)
przekladnia = (2 * N * kfs / kfr) ** 2 * (3 / Qr)
Rc = Rc * przekladnia
kRv = 0.01 * h * np.sqrt(frv)
Rpr = ((lpr / float(1e3)) / (gammar_teta * spr))
Rpr = Rpr * przekladnia
Rprv = Rpr * kRv
Rcv = 2 * Rc + Rprv * (2 * np.sin(alfaQv / 2)) ** 2
Ldeltac = (mi0 * (lFe / 1000) * ((tr - bsr) / 1000)) / ((delta / 1000) * kCs)

kX = np.ones(frv.size)
for i, value in enumerate(frv):
    if h >= (150 / np.sqrt(value)):
        kX[i] = 150 / (h * np.sqrt(value))

frpodst = np.min(frv)
Lqra01 = Xqra01 / (2*pi*frpodst)
Lqra01 = Lqra01 * przekladnia
Lpr = Xpr / (2*pi*frpodst)
Lpr = Lpr * przekladnia
LQrv = Lqra01 + Lpr * kX
LQcv = LQrv * (2*np.sin(alfaQv/2))**2
Icv = Uicv / (np.sqrt(Rcv**2 + (2*pi*frv * (LQcv + Ldeltac)**2)))
Iprv = Icv * 2 * np.sin(alfaQv / 2)

    # np.savetxt("rzad_vs_Debug.csv", rzad_vs, fmt='%.3e', delimiter = ",")
    # np.savetxt("sum_Bs_Debug.csv", sum_Bs, fmt='%.3e', delimiter = ",")
    # np.savetxt("new_vs_Debug.csv", new_vs, fmt='%.3e', delimiter = ",")
    # np.savetxt("temp_Bs_Debug.csv", temp_Bs, fmt='%.3e', delimiter = ",")

    # with open('debug.txt', 'w') as f:
    #     print(rzad_vs, file=f)
    #     print(sum_Bs, file=f)
    #     print('*' * 50)
    #     print(new_vs, file=f)
    #     print(temp_Bs, file=f)

    # while True:
    #     print(rzad_vs)

    # for i, item in enumerate(rzad_vs):
    #     # print(i, item)
    #     ind = np.where(rzad_vs[i+1:] == item)[0]
    #     if ind.size != 0:
    #         dupl_ind = ind + (i+1)
    #         print(dupl_ind, rzad_vs[dupl_ind])
    #
    # if x.size != 0:
    #     print(x[0])
