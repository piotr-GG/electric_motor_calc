import numpy as np


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
            self.__order = array
        else:
            raise ValueError("Argument is not an instance of ndarray!")

    @property
    def flux_dens(self):
        return self.__flux_dens

    @flux_dens.setter
    def flux_dens(self, array):
        if isinstance(array, np.ndarray):
            self.__flux_dens = array
        else:
            raise ValueError("Argument is not an instance of ndarray!")

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


if __name__ == "__main__":
    Bls = FluxDensity(np.array([1, 2, 3]), np.array([1, 2, 3]))
    print(Bls)
    Brs = FluxDensity(np.array([6, 5, 3]), np.array([1, 2, 3]))