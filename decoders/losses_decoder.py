import json

from model.flux_density import FluxDensity
from model.losses import Losses
import numpy as np


class LossesDecoder:
    def __init__(self, encoded_data):
        if isinstance(encoded_data, dict):
            self.data = encoded_data
        else:
            raise json.JSONDecodeError

    def decode(self):
        try:
            self.limit = self.data["Limit"]
            self.kls = self.data["kls"]
            self.klr = self.data["klr"]
            self.gs = self.data["gs"]
            self.gr = self.data["gr"]
            self.Ps = self.data["Ps"]
            self.PAl = self.data["PAl"]
            self.Pss = self.data["Pss"]
            self.Pp = self.data["Pp"]
            self.stator_losses = self.data["stator_losses"]
            self.vs = self.stator_losses["vs"]
            self.psv = self.stator_losses["psv"]
            self.palv = self.stator_losses["palv"]
            self.stator_losses = (Losses(np.array(self.vs, dtype=int), np.array(self.psv, dtype="float64")),
                                  Losses(np.array(self.vs, dtype=int), np.array(self.palv, dtype="float64")))

            self.rotor_losses = self.data["rotor_losses"]
            self.vr = self.rotor_losses["vr"]
            self.pssv = self.rotor_losses["pssv"]
            self.ppv = self.rotor_losses["ppv"]
            self.rotor_losses = (Losses(np.array(self.vr, dtype=int), np.array(self.pssv, dtype="float64")),
                                 Losses(np.array(self.vr, dtype=int), np.array(self.ppv, dtype="float64")))

            self.stator_fluxes = self.data["stator_fluxes"]
            self.vs = self.stator_fluxes["vs"]
            self.Bs = self.stator_fluxes["Bs"]
            self.stator_fluxes = (FluxDensity(np.array(self.vs, dtype=int), np.array(self.Bs, dtype="float64")))

            self.rotor_fluxes = self.data["rotor_fluxes"]
            self.vr = self.rotor_fluxes["vr"]
            self.Br = self.rotor_fluxes["Br"]
            self.rotor_fluxes = (FluxDensity(np.array(self.vr, dtype=int), np.array(self.Br, dtype="float64")))

        except KeyError:
            raise json.JSONDecodeError
        return self.limit, self.kls, self.klr, self.gs, self.gr, self.Ps, self.PAl, self.Pss, self.Pp, \
            self.stator_losses, self.rotor_losses, self.stator_fluxes, self.rotor_fluxes

    def printDecoded(self):
        print("Limit =", self.limit)
        print("kls =", self.kls)
        print("klr =", self.klr)
        print("gs =", self.gs)
        print("gr =", self.gr)
        print("Ps =", self.Ps)
        print("PAl =", self.PAl)
        print("Pss =", self.Pss)
        print("Pp = ", self.Pp)
        print("Stator losses[0]\n", self.stator_losses[0])
        print("Stator losses[1]\n", self.stator_losses[1])
        print("Rotor losses[0]\n", self.rotor_losses[0])
        print("Rotor losses[1]\n", self.rotor_losses[1])

        print(sum(self.stator_losses[0].losses))
        print(sum(self.stator_losses[1].losses))
        print(sum(self.rotor_losses[0].losses))
        print(sum(self.rotor_losses[1].losses))
