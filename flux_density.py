from elmag_container import ElectromagContainer
import numpy as np


# TODO: Add sorted() to method returning fluxes and orders

class FluxDensity(ElectromagContainer):
    def __init__(self, order, flux_dens):
        super(FluxDensity, self).__init__(order, flux_dens)

    @property
    def flux_dens(self):
        return self.elmag_qty

    @flux_dens.setter
    def flux_dens(self, array):
        self.elmag_qty = array

    def __add__(self, other):
        if isinstance(self, FluxDensity) and isinstance(other, FluxDensity):
            return super(FluxDensity, self).__add__(other)
        else:
            raise TypeError("One of the operands is not an instance of FluxDensity")

    def __eq__(self, other):
        if isinstance(self, FluxDensity) and isinstance(other, FluxDensity):
            return super(FluxDensity, self).__eq__(other)
        else:
            raise TypeError("Wrong operands type!")


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
