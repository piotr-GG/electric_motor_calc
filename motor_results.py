from motor_calc import MotorCalc
from motor import Motor
import datetime as dt


class MotorResults:
    """
    Class used to save calculation results to file / json / DB
    """

    def __init__(self, motor_calc):
        if isinstance(motor_calc, MotorCalc):
            self.__motor_calc = motor_calc
        else:
            raise ValueError("Argument motor_calc shall be an instance of MotorCalc class")

    @property
    def motor_calc(self):
        return self.__motor_calc

    @motor_calc.setter
    def motor_calc(self, value):
        if isinstance(value, MotorCalc):
            self.__motor_calc = value
        else:
            raise ValueError("Wrong argument for assignement (not an instance of MotorClass")

    def save_to_json(self):
        pass

    def load_from_json(self):
        pass

    def save_to_file(self, filename: str = ""):
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
        return True

    def load_from_file(self):
        pass

    def save_to_DB(self):
        pass

    def load_to_DB(self):
        pass


if __name__ == "__main__":
    m = Motor()
    m_calc = MotorCalc(m, 5)
    m_calc.calculate()
    m_res = MotorResults(m_calc)
    m_res.save_to_file()
