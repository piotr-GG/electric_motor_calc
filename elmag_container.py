import numpy as np


class ElectromagContainer:
    def __init__(self, order, elmag_qty):
        self.order = order
        self.elmag_qty = elmag_qty

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
    def elmag_qty(self):
        return self.__elmag_qty

    @elmag_qty.setter
    def elmag_qty(self, array):
        if isinstance(array, np.ndarray):
            self.__elmag_qty = np.around(array, decimals=6)
        else:
            raise ValueError("Argument is not an instance of ndarray!")

    def sort(self, ascending:bool = True):
        sorted_vals = sorted(zip(self.order, self.elmag_qty), key=lambda s: s[0], reverse=not ascending)
        unzipped_vals = list(zip(*sorted_vals))
        self.order = np.array(unzipped_vals[0], dtype="int32")
        self.elmag_qty = np.array(unzipped_vals[1], dtype="float64")

    def __str__(self):
        txt = ""
        for o, elm_q in zip(self.order, self.elmag_qty):
            txt += str(o) + " : " + str(elm_q) + "\n"
        return txt

    def __add__(self, other):
        if isinstance(self, ElectromagContainer) and isinstance(other, ElectromagContainer):
            if self.order.size == self.elmag_qty.size and other.order.size == other.elmag_qty.size:
                self.order = np.hstack((self.order, other.order))
                self.elmag_qty = np.hstack((self.elmag_qty, other.elmag_qty))
            else:
                raise ValueError("One of the operands has inconsistent number of elements (order != flux_dens")
        else:
            raise TypeError("One of the operands is not an instance of FluxDensity")
        return self

    def __eq__(self, other):
        if not isinstance(other, ElectromagContainer):
            return False
        else:
            return np.allclose(self.order, other.order) and np.allclose(self.elmag_qty, other.elmag_qty)
