import numpy as np


# TODO: Add sorted() to method returning fluxes and orders

class FluxDensity:
    def __init__(self, order, flux_dens):
        self.order = order
        self.flux_dens = flux_dens

    @property
    def order(self):
        return self.__order

    @order.setter
    def order(self, array):
        if isinstance(array, np.ndarray):
            if array.dtype != "int32":
                self.__order = array.astype(int)
            else:
                self.__order = array
        else:
            raise ValueError("Argument is not an instance of ndarray!")

    @property
    def flux_dens(self):
        return self.__flux_dens

    @flux_dens.setter
    def flux_dens(self, array):
        if isinstance(array, np.ndarray):
            self.__flux_dens = np.around(array, decimals=6)
        else:
            raise ValueError("Argument is not an instance of ndarray!")

    def sort(self, ascending: bool = True):
        sorted_vals = sorted(zip(self.order, self.flux_dens), key=lambda s: s[0], reverse=not ascending)
        unzipped_vals = list(zip(*sorted_vals))
        self.order = np.array(unzipped_vals[0], dtype="int32")
        self.flux_dens = np.array(unzipped_vals[1], dtype="float64")

        # zipped_vals = zip(self.order, self.flux_dens)
        # print("Zipped vals = ", zipped_vals)
        # sorted_vals = sorted(zip(self.order, self.flux_dens), key=lambda s: s[0])
        # print("Sorted vals = ", sorted_vals)
        # unzipped_vals = list(zip(*sorted_vals))
        # print("Unzipped vals", unzipped_vals)
        # order = np.array(unzipped_vals[0], dtype="int")
        # flux_d = np.array(unzipped_vals[1], dtype="float64")
        # print("Order = ", order, "dtype = ", order.dtype)
        # print("Flux = ", flux_d, "dtype = ", flux_d.dtype)
        # print("Type(order) =", type(order))
        # print("Type(flux_d)=", type(flux_d))
        # # print("Unzippedvals[0]= ", np.array(unzipped_vals[0], dtype="int"), "type =", type(unzipped_vals[0]))
        # # print("Unzippedvals[1]= ", unzipped_vals[1], "type =", type(unzipped_vals[1]))

    def __str__(self):
        txt = ""
        for o, fd in zip(self.order, self.flux_dens):
            txt += str(o) + " : " + str(fd) + "\n"
        return txt

    def __add__(self, other):
        if isinstance(self, FluxDensity) and isinstance(other, FluxDensity):
            if self.order.size == self.flux_dens.size and other.order.size == other.flux_dens.size:
                self.order = np.hstack((self.order, other.order))
                self.flux_dens = np.hstack((self.flux_dens, other.flux_dens))
            else:
                raise ValueError("One of the operands has inconsistent number of elements (order != flux_dens")
        else:
            raise TypeError("One of the operands is not an instance of FluxDensity")
        return self

    def __eq__(self, other):
        if not isinstance(other, FluxDensity):
            return False
        else:
            return np.allclose(self.order, other.order) and np.allclose(self.flux_dens, other.flux_dens)


if __name__ == "__main__":
    Bls = FluxDensity(np.array([1.0, 2.0, 3.0, -2.0, -3.0, -88, -23]), np.array([1.0, 2.3, 3.9, -5, -4, -82, -20]))
    Bls.sort()
    print(Bls)
    # print(Bls)
    # print(len(Bls.order))
    # Brs = FluxDensity(np.array([6, 5, 3]), np.array([1, 2, 3]))
    # print(list((Bls.order, Bls.flux_dens)))
    # lista = zip(Bls.order, Bls.flux_dens)
    # print(lista)
    # print("Sortowanie")
    # posortowane = sorted(lista, key=lambda s: s[0])
    # print(list(zip(*posortowane)))
