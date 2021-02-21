from collections import OrderedDict

from json import JSONDecodeError
from data_transfer.data_storage_interface import DataStorageInterface
from model.motor_calc import MotorCalc
from model.motor_results import LoadFileError
from decoders.losses_decoder import LossesDecoder
import json
from definitions import ROOT_DIR
import datetime as dt
from encoders.NumpyEncoder import NumpyEncoder


class JSONDataTransfer(DataStorageInterface):
    @staticmethod
    def import_data(destination: str):
        if destination is None:
            raise LoadFileError("Filename is empty!")
        with open(destination, 'r') as f:
            try:
                data = json.load(f)
                decoder = LossesDecoder(data)
                return decoder.decode()

            except JSONDecodeError:
                return "FILE BEING LOADED IS NOT AN VALID JSON FILE!"

    @staticmethod
    def export_data(data: MotorCalc, destination: str):
        if destination == "":
            destination = "results_" + dt.datetime.today().strftime("%d-%m-%y %X").replace(":", ".")
        keys = ["Limit", "kls", "klr", "gs", "gr", "Ps", "PAl", "Pss", "Pp", "stator_losses", "rotor_losses",
                "stator_fluxes", "rotor_fluxes"]

        stator_losses = data.stator_losses_serializable()
        rotor_losses = data.rotor_losses_serializable()
        stator_fluxes = data.stator_fluxes_serializable()
        rotor_fluxes = data.rotor_fluxes_serializable()

        vals = [data.limit, data.kls_, data.klr_, data.gs_, data.gr_, data.Ps, data.PAl,
                data.Pss, data.Pp, stator_losses, rotor_losses, stator_fluxes, rotor_fluxes]

        f_cont = OrderedDict(zip(keys, vals))

        if not destination.endswith(".json"):
            destination += ".json"

        dir_to_open = ROOT_DIR + f"/json/{destination}"
        result = 0

        print(f_cont)
        print(destination)
        print(data)
        with open(dir_to_open, "w+") as f:
            result = f.write(json.dumps(f_cont, cls=NumpyEncoder))
        return result != 0
