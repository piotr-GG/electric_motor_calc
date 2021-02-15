from PyQt5 import QtWidgets

from gui.main_gui import MainGUI
from model.motor_calc import MotorCalc
from model.motor import Motor
from model.motor_results import MotorResults
from utils.utils import Utils

if __name__ == "__main__":
    import sys

    sys.excepthook = Utils.excepthook_errormsg
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MainGUI()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


