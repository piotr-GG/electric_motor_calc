from motor_calc import MotorCalc
from motor import Motor
from db_conn import DBConnection, DBCreationError
import datetime as dt
from encoders.NumpyEncoder import NumpyEncoder
import json
from json import JSONDecodeError
from collections import OrderedDict
from decoders.LossesDecoder import LossesDecoder
from definitions import ROOT_DIR


class LoadFileError(Exception):
    pass


class MotorResults:
    """
    Class used to save / load calculation results to / from file / json / DB
    """

    def __init__(self, motor_calc):
        if isinstance(motor_calc, MotorCalc):
            self.__motor_calc = motor_calc
        else:
            raise ValueError("Argument motor_calc shall be an instance of MotorCalc class")
        self.__db_path = "db/results.db"

    @property
    def motor_calc(self):
        return self.__motor_calc

    @motor_calc.setter
    def motor_calc(self, value):
        if isinstance(value, MotorCalc):
            self.__motor_calc = value
        else:
            raise ValueError("Wrong argument for assignment (not an instance of MotorClass")

    @property
    def db_path(self):
        return self.__db_path

    @db_path.setter
    def db_path(self, new_db_path):
        self.__db_path = new_db_path

    def save_to_json(self, filename: str = "") -> bool:
        if filename == "":
            filename = "results_" + dt.datetime.today().strftime("%d-%m-%y %X").replace(":", ".")
        keys = ["Limit", "Ps", "PAl", "Pss", "Pp", "stator_losses", "rotor_losses"]

        stator_losses = self.motor_calc.stator_losses_serializable()
        rotor_losses = self.motor_calc.rotor_losses_serializable()

        vals = [self.motor_calc.limit, self.motor_calc.Ps, self.motor_calc.PAl,
                self.motor_calc.Pss, self.motor_calc.Pp, stator_losses, rotor_losses]

        f_cont = OrderedDict(zip(keys, vals))

        if not filename.endswith(".json"):
            filename += ".json"

        dir_to_open = ROOT_DIR + f"/json/{filename}"
        result = 0
        with open(dir_to_open, "w+") as f:
            result = f.write(json.dumps(f_cont, cls=NumpyEncoder))
        return result != 0

    def load_from_json(self, filename: str) -> str:
        if filename is None:
            raise LoadFileError("Filename is empty!")
        with open(filename, 'r') as f:
            try:
                data = json.load(f)
                decoder = LossesDecoder(data)
                return decoder.decode()

            except JSONDecodeError:
                return "FILE BEING LOADED IS NOT AN VALID JSON FILE!"

    def save_to_file(self, filename: str = "") -> None:
        """
        Saves the motor calculation results into a file. If no filename parameter is given, the default value is assumend.
        :param filename: str
        :return: boolean
        """
        if filename == "":
            filename = "results_" + dt.datetime.today().strftime('%d-%m-%y %X').replace(':', '.') + ".txt"

        with open(f'results/{filename}', 'w') as f:
            f.write(f"Limit ={self.motor_calc.limit}\n")
            f.write(f"Ps = {self.motor_calc.Ps}\n")
            f.write(f"PAl = {self.motor_calc.PAl}\n")
            f.write(f"Pss = {self.motor_calc.Pss}\n")
            f.write(f"Pp = {self.motor_calc.Pp}\n")

    def load_from_file(self, filename: str) -> str:
        """
        Load contents from file.
        :param filename: name of file to be loaded.
        :return: str
        """
        if filename is None:
            raise LoadFileError("Filename is empty!")
        with open(filename, 'r') as f:
            f_cont = f.read()
        return f_cont

    def save_to_DB(self) -> bool:
        """
            Saves the motor calculation results to DB
            :return: bool
        """
        db_path = "db/results.db"
        try:
            db_conn = DBConnection(db_path)
        except DBCreationError:
            print("Something went wrong during DB creation")
            return False
        vars_to_save = (self.motor_calc.limit, self.motor_calc.Ps, self.motor_calc.PAl,
                        self.motor_calc.Pss, self.motor_calc.Pp)

        db_conn.insertValueIntoMotorResults(vars_to_save)
        db_conn.close_conn()
        return True

    def load_from_DB(self, id: int) -> list:
        """
        Loads motor results by given id.
        :param id: Specifies id to be retrieved from DB. If id = 0, then all the results are fetched.
        :return: list
        """
        db_path = "db/results.db"
        try:
            db_conn = DBConnection(db_path)
        except DBCreationError:
            print("Something went wrong during DB creation")
            return []
        if id == 0:
            return db_conn.getResults()
        elif id > 0:
            return db_conn.getSingleResult(id)
        db_conn.close_conn()

    def __str__(self):
        return self.__motor_calc.__str__()


if __name__ == "__main__":
    m = Motor()
    m_calc = MotorCalc(m, limit=15)
    m_calc.calculate()
    m_res = MotorResults(m_calc)

    m_res.save_to_json("test_3")

    # limit, Ps, PAl, Pss, Pp, stator_losses, rotor_losses = \
    #     loaded_json = m_res.load_from_json(r'json/testowy_1.json')

    # loaded_json = OrderedDict(loaded_json)
    # for k, v in loaded_json.items():
    #     print(k, v)

    # print(m_res.load_from_file(r'results/results_25-01-21 21.20.29.txt').splitlines())

    # m_res.save_to_DB()
    # m_res.save_to_DB()
    # print(m_res.load_from_DB(0))

    # m_res.save_to_file()
    # m_res.save_to_json()

    # loaded_json = m_res.load_from_json(r'json/results_25-01-21 21.20.58.json')
    # loaded_json = OrderedDict(loaded_json)
    # for k, v in loaded_json.items():
    #     print(k, v)
    # print(m_res.load_from_file(r'results/results_25-01-21 21.20.29.txt').splitlines())
