import pandas as pd
from definitions import ROOT_DIR
from model.motor import Motor


class ExcelParser:
    def __init__(self, xl_file):
        if not xl_file.endswith(".xlsx"):
            xl_file += ".xlsx"
        self.data = pd.read_excel(ROOT_DIR + "/xlsx/" + xl_file, usecols=["Parametr", "Wartość"], index_col=None)
        self.data["Parametr"] = self.data["Parametr"].str.strip()

        self.df = pd.DataFrame(self.data, columns=['Parametr', 'Wartość'], index=None)
        self.data_dict = dict(self.df.to_dict(orient="split")['data'])

    @property
    def data_dict(self):
        return self.__data_dict

    @data_dict.setter
    def data_dict(self, val):
        self.__data_dict = val

    def printData(self):
        for k, v in self.data_dict.items():
            print(k, "=", v, " type=", type(v))


if __name__ == "__main__":
    xlParser = ExcelParser("params")
    xlParser.printData()
    motor = Motor(val_dict=xlParser.data_dict)
    print(motor.p)