import math
from utils import Utils


class Motor:
    """
    Most basic class for instantiating a motor object and providing several basic methods
    """

    def __init__(self, val_dict=None):
        if val_dict is None:
            self.initDefaultVals()
        else:
            self.initFromDict(val_dict)

    def initDefaultVals(self):
        self.p = 2  # Liczba par biegunów [-]
        self.Qs = 36  # Liczba żłobków stojana [-]
        self.Qr = 28  # Liczba żłobków wirnika [-]
        self.W = 9  # Liczba żłobków oddzielająca od siebie prawy i lewy bok zezwoju [-]
        self.bss = 3.6  # Szerokość szczerbiny żłobka stojana [mm]
        self.bsr = 1  # Szerokość szczerbiny żłobka wirnika [mm]
        self.bts = 9.83  # Szerokosc zeba stojana [mm]
        self.btr = 16.18  # Szerokosc zeba wirnika [mm]
        self.delta = 0.45  # Szerokość szczeliny powietrznej [mm]
        self.N = 141  # Liczba zwojów uzwojenia [-]
        self.m = 3  # Liczba pasm uzwojenia [-]
        self.ds = 154  # Szerokość zewnętrzna stojana [mm]
        self.dr = self.ds - 2 * self.delta  # Szerokość zewnętrzna wirnika [mm]
        self.s = 6  # Liczba stref boków uzwojenia na parę biegunów / stref pasmowych na przestrzeni pary biegunów [-]
        self.Bdelta = 0.7424  # Indukcja w szczelinie powietrznej [T]
        self.mi0 = 1.257 * 10 ** -6  # Przenikalnosc magnetyczna prozni
        self.cosfi = 0.84  # Wspolczynnik mocy [-]
        self.sinfi = math.sqrt(1 - self.cosfi ** 2)  # Sinus fi [-]
        self.s_p = 0.01937  # Poślizg [-]
        self.fs = 50  # Częstotliwośc napiecia zasilajacego [Hz]
        self.roFe = 7.8  # Gęstosc (masa wlasciwa) materialu rdzenia [kg/dm3]
        self.lFe = 199  # Dlugosc pakietu silnika [mm]
        self.pCl = 4.5  # Gestosc strat z pradow wirowych przy 50Hz i 1,5 T [W/kg]
        self.kFe = 0.96  # Wspolczynnik zapelnienia zelaza [-]
        self.lpr = 190  # Dlugosc preta [mm]
        self.spr = 165  # Przekroj preta [mm^2]
        self.h = 37  # Wysokosc preta [mm]
        self.Rc = 1000  # Rezystancja klatki [Ohm]
        self.ks = 1  # Wspolczynnik szczerbiny wynikajacy z rozkladu okladu pradowego na szerokosci szczerbiny [-]
        self.mts = 9.18  # Masa zebow stojana [kg]
        self.Is = 28.66  # Prąd przewodowy pobierany z sieci [A]
        self.I0 = 13.09  # Prad przewodowy biegu jalowego [A]
        self.Isph = self.Is / math.sqrt(3)  # Prąd fazowy pobierany z sieci [A]
        self.I0ph = self.I0 / math.sqrt(3)  # Prad fazowy biegu jalowego [A]
        self.Ipr = 411  # Prąd w pręcie klatki wirnika [A]
        self.Vp = 374.9  # Napiecie magnetyczne w szczelinie [A]
        self.Vsd = 50.57  # Napiecie magnetyczne w zebach [A]
        self.km = 1 + self.Vsd / self.Vp  # Współczynnik nasycenia obwodu magnetycznego [-]
        self.gammar_0 = 35  # przewodnosc cieplna materialu preta klatki wirnika w temperaturze 20 deg C [Sm / mm^2]
        self.tetar = 135  # Temperatura uzwojenia wirnika przyjeta do obliczen [deg C]
        self.kgamma = 225  # Wspolczynnik do obliczenia przewodnosci cieplnej w temperaturze tetar [-]
        self.dc = 110  # Srednica pierscienia zwierajacego klatke wirnika [mm]
        self.sc = 800  # Przekroj pierscienia zwierajacego klatke wirnika [mm2]

        self.Xqra01 = 5.9276e-05  # Reaktancja niepodlegajaca wypieraniu pradu, niesprowadzona
        self.Xpr = 0.00017001  # Reaktancja podlegajaca wypieraniu pradu, sprowadzona

    def initFromDict(self, val_dict: dict):
        try:
            self.p = val_dict["p"]
            self.Qs = val_dict["Qs"]
            self.Qr = val_dict["Qr"]
            self.W = val_dict["W"]
            self.bss = val_dict["bss"]
            self.bsr = val_dict["bsr"]
            self.bts = val_dict["bts"]
            self.btr = val_dict["btr"]
            self.delta = val_dict["delta"]
            self.N = val_dict["N"]
            self.m = val_dict["m"]
            self.ds = val_dict["ds"]
            self.dr = self.ds - 2 * self.delta  # Szerokość zewnętrzna wirnika [mm]
            self.s = val_dict["s"]
            self.Bdelta = val_dict["Bdelta"]
            self.mi0 = 1.257 * 10 ** -6  # Przenikalnosc magnetyczna prozni
            self.cosfi = val_dict["cosfi"]
            self.sinfi = math.sqrt(1 - self.cosfi ** 2)  # Sinus fi [-]
            self.s_p = val_dict["s_p"]
            self.fs = val_dict["fs"]
            self.roFe =  val_dict["roFe"]
            self.lFe = val_dict["lFe"]
            self.pCl = val_dict["pCl"]
            self.kFe = val_dict["kFe"]
            self.lpr = val_dict["lpr"]
            self.spr = val_dict["spr"]
            self.h = val_dict["h"]
            self.Rc = val_dict["Rc"]
            self.ks = val_dict["ks"]
            self.mts = val_dict["mts"]
            self.Is = val_dict["Is"]
            self.I0 = val_dict["I0"]
            self.Isph = self.Is / math.sqrt(3)  # Prąd fazowy pobierany z sieci [A]
            self.I0ph = self.I0 / math.sqrt(3)  # Prad fazowy biegu jalowego [A]
            self.Ipr = val_dict["Ipr"]
            self.Vp = val_dict["Vp"]
            self.Vsd = val_dict["Vsd"]
            self.km = 1 + self.Vsd / self.Vp  # Współczynnik nasycenia obwodu magnetycznego [-]
            self.gammar_0 = val_dict["gammar_0"]
            self.tetar = val_dict["tetar"]
            self.kgamma = val_dict["kgamma"]
            self.dc = val_dict["dc"]
            self.sc = val_dict["sc"]

            self.Xqra01 = val_dict["Xqra01"]
            self.Xpr = val_dict["Xpr"]
            # for k, v in val_dict.items():
            #     print(k, v)
        except KeyError:
            Utils.show_error_box("Błąd",
                                 "W trakcie importu danych silnika z Excela wystąpił błąd: "
                                 "Nie znaleziono danego parametru")

    def __str__(self):
        txt = ""
        txt += "p  = " + str(self.p) + "\n"
        txt += "Qs = " + str(self.Qs) + "\n"
        txt += "Qr = " + str(self.Qr) + "\n"
        txt += "W  = " + str(self.W) + "\n"
        txt += "bss = " + str(self.bss) + "\n"
        txt += "bsr = " + str(self.bsr) + "\n"
        txt += "bts = " + str(self.bts) + "\n"
        txt += "btr = " + str(self.btr) + "\n"
        txt += "delta = " + str(self.delta) + "\n"
        txt += "N = " + str(self.N)
        return txt

    @property
    def p(self):
        return self.__p

    @p.setter
    def p(self, val):
        self.__p = int(val)

    @property
    def Qs(self):
        return self.__Qs

    @Qs.setter
    def Qs(self, val):
        self.__Qs = int(val)

    @property
    def Qr(self):
        return self.__Qr

    @Qr.setter
    def Qr(self, val):
        self.__Qr = int(val)

    @property
    def W(self):
        return self.__W

    @W.setter
    def W(self, value):
        self.__W = int(value)

    @property
    def bss(self):
        return self.__bss

    @bss.setter
    def bss(self, value):
        self.__bss = value

    @property
    def bsr(self):
        return self.__bsr

    @bsr.setter
    def bsr(self, value):
        self.__bsr = value

    @property
    def bts(self):
        return self.__bts

    @bts.setter
    def bts(self, value):
        self.__bts = value

    @property
    def btr(self):
        return self.__btr

    @btr.setter
    def btr(self, value):
        self.__btr = value

    @property
    def delta(self):
        return self.__delta

    @delta.setter
    def delta(self, value):
        self.__delta = value

    @property
    def N(self):
        return self.__N

    @N.setter
    def N(self, value):
        self.__N = int(value)

    @property
    def m(self):
        return self.__m

    @m.setter
    def m(self, value):
        self.__m = int(value)

    @property
    def ds(self):
        return self.__ds

    @ds.setter
    def ds(self, value):
        self.__ds = value

    @property
    def dr(self):
        return self.__dr

    @dr.setter
    def dr(self, value):
        self.__dr = value

    @property
    def s(self):
        return self.__s

    @s.setter
    def s(self, value):
        self.__s = int(value)

    @property
    def Bdelta(self):
        return self.__Bdelta

    @Bdelta.setter
    def Bdelta(self, value):
        self.__Bdelta = value

    @property
    def mi0(self):
        return self.__mi0

    @mi0.setter
    def mi0(self, value):
        self.__mi0 = value

    @property
    def cosfi(self):
        return self.__cosfi

    @cosfi.setter
    def cosfi(self, value):
        self.__cosfi = value

    @property
    def sinfi(self):
        return self.__sinfi

    @sinfi.setter
    def sinfi(self, value):
        self.__sinfi = value

    @property
    def s_p(self):
        return self.__s_p

    @s_p.setter
    def s_p(self, value):
        self.__s_p = value

    @property
    def fs(self):
        return self.__fs

    @fs.setter
    def fs(self, value):
        self.__fs = value

    @property
    def roFe(self):
        return self.__roFe

    @roFe.setter
    def roFe(self, value):
        self.__roFe = value

    @property
    def lFe(self):
        return self.__lFe

    @lFe.setter
    def lFe(self, value):
        self.__lFe = value

    @property
    def pCl(self):
        return self.__pCl

    @pCl.setter
    def pCl(self, value):
        self.__pCl = value

    @property
    def kFe(self):
        return self.__kFe

    @kFe.setter
    def kFe(self, value):
        self.__kFe = value

    @property
    def lpr(self):
        return self.__lpr

    @lpr.setter
    def lpr(self, value):
        self.__lpr = value

    @property
    def spr(self):
        return self.__spr

    @spr.setter
    def spr(self, value):
        self.__spr = value

    @property
    def h(self):
        return self.__h

    @h.setter
    def h(self, value):
        self.__h = value

    @property
    def Rc(self):
        return self.__Rc

    @Rc.setter
    def Rc(self, value):
        self.__Rc = value

    @property
    def ks(self):
        return self.__ks

    @ks.setter
    def ks(self, value):
        self.__ks = value

    @property
    def mts(self):
        return self.__mts

    @mts.setter
    def mts(self, value):
        self.__mts = value

    @property
    def Is(self):
        return self.__Is

    @Is.setter
    def Is(self, value):
        self.__Is = value

    @property
    def I0(self):
        return self.__I0

    @I0.setter
    def I0(self, value):
        self.__I0 = value

    @property
    def Isph(self):
        return self.__Isph

    @Isph.setter
    def Isph(self, value):
        self.__Isph = value

    @property
    def I0ph(self):
        return self.__I0ph

    @I0ph.setter
    def I0ph(self, value):
        self.__I0ph = value

    @property
    def Ipr(self):
        return self.__Ipr

    @Ipr.setter
    def Ipr(self, value):
        self.__Ipr = value

    @property
    def Vp(self):
        return self.__Vp

    @Vp.setter
    def Vp(self, value):
        self.__Vp = value

    @property
    def Vsd(self):
        return self.__Vsd

    @Vsd.setter
    def Vsd(self, value):
        self.__Vsd = value

    @property
    def km(self):
        return self.__km

    @km.setter
    def km(self, value):
        self.__km = value

    @property
    def gammar_0(self):
        return self.__gammar_0

    @gammar_0.setter
    def gammar_0(self, value):
        self.__gammar_0 = value

    @property
    def tetar(self):
        return self.__tetar

    @tetar.setter
    def tetar(self, value):
        self.__tetar = value

    @property
    def kgamma(self):
        return self.__kgamma

    @kgamma.setter
    def kgamma(self, value):
        self.__kgamma = value

    @property
    def dc(self):
        return self.__dc

    @dc.setter
    def dc(self, value):
        self.__dc = value

    @property
    def sc(self):
        return self.__sc

    @sc.setter
    def sc(self, value):
        self.__sc = value

    @property
    def Xqra01(self):
        return self.__Xqra01

    @Xqra01.setter
    def Xqra01(self, value):
        self.__Xqra01 = value

    @property
    def Xpr(self):
        return self.__Xpr

    @Xpr.setter
    def Xpr(self, value):
        self.__Xpr = value


if __name__ == "__main__":
    m = Motor()
    print(m)
