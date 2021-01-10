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
ksv = np.sin(vs*bss/ds) / (vs*bss/ds)
print_var_value(ksv, 'ksv')
kfv = kqv * kyv * ksv
print_var_value(kfv, 'kfv')
ky1 = np.sin((p/p) * y * (pi / 2))
print_var_value(ky1,'ky1')
ks1 = np.sin(p*bss/ds) / (p*bss/ds)
print_var_value(ks1, 'ks1')
kq1 = np.sin((p/p) * (pi/6))/(qc*np.sin((p/p)* (pi/(6*qc))))
print_var_value(kq1, 'kq1')
kfs = ky1 * ks1 * kq1
print_var_value(kfs, 'kfs')
