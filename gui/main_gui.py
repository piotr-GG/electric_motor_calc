# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from results_tab import CalcResultsWidget
from motor_calc import MotorCalc
from motor import Motor
from motor_results import MotorResults
from utils import Utils


class UiMainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(450, 400))
        MainWindow.setMaximumSize(QtCore.QSize(600, 400))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(240, 20, 81, 117))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(7)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.ks_val_qle = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.ks_val_qle.setObjectName("ks_val_qle")
        self.horizontalLayout.addWidget(self.ks_val_qle)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.kr_val_qle = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.kr_val_qle.setObjectName("kr_val_qle")
        self.horizontalLayout_2.addWidget(self.kr_val_qle)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.gs_val_qle = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.gs_val_qle.setObjectName("gs_val_qle")
        self.horizontalLayout_3.addWidget(self.gs_val_qle)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.gr_val_qle = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.gr_val_qle.setObjectName("gr_val_qle")
        self.horizontalLayout_4.addWidget(self.gr_val_qle)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(120, 160, 321, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(15)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.groupBox = QtWidgets.QGroupBox(self.horizontalLayoutWidget)
        self.groupBox.setObjectName("groupBox")
        self.db_save_pbtn = QtWidgets.QPushButton(self.groupBox)
        self.db_save_pbtn.setGeometry(QtCore.QRect(20, 20, 75, 23))
        self.db_save_pbtn.setObjectName("db_save_pbtn")
        self.db_load_pbtn = QtWidgets.QPushButton(self.groupBox)
        self.db_load_pbtn.setGeometry(QtCore.QRect(20, 50, 75, 23))
        self.db_load_pbtn.setObjectName("db_load_pbtn")
        self.horizontalLayout_5.addWidget(self.groupBox)
        self.groupBox_3 = QtWidgets.QGroupBox(self.horizontalLayoutWidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.txt_save_pbtn = QtWidgets.QPushButton(self.groupBox_3)
        self.txt_save_pbtn.setGeometry(QtCore.QRect(20, 20, 75, 23))
        self.txt_save_pbtn.setObjectName("txt_save_pbtn")
        self.txt_load_pbtn = QtWidgets.QPushButton(self.groupBox_3)
        self.txt_load_pbtn.setGeometry(QtCore.QRect(20, 50, 75, 23))
        self.txt_load_pbtn.setObjectName("txt_load_pbtn")
        self.horizontalLayout_5.addWidget(self.groupBox_3)
        self.groupBox_2 = QtWidgets.QGroupBox(self.horizontalLayoutWidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.json_load_ptbn = QtWidgets.QPushButton(self.groupBox_2)
        self.json_load_ptbn.setGeometry(QtCore.QRect(20, 50, 75, 23))
        self.json_load_ptbn.setObjectName("json_load_ptbn")
        self.json_save_pbtn = QtWidgets.QPushButton(self.groupBox_2)
        self.json_save_pbtn.setGeometry(QtCore.QRect(20, 20, 75, 23))
        self.json_save_pbtn.setObjectName("json_save_pbtn")
        self.horizontalLayout_5.addWidget(self.groupBox_2)
        self.calculate_pbtn = QtWidgets.QPushButton(self.centralwidget)
        self.calculate_pbtn.setGeometry(QtCore.QRect(200, 260, 161, 31))
        self.calculate_pbtn.setObjectName("calculate_pbtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        self.menuZamknij = QtWidgets.QMenu(self.menubar)
        self.menuZamknij.setObjectName("menuZamknij")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOtw_rz = QtWidgets.QAction(MainWindow)
        self.actionOtw_rz.setObjectName("actionOtw_rz")
        self.menuZamknij.addAction(self.actionOtw_rz)
        self.menubar.addAction(self.menuZamknij.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Setup custom variables and attributes
        self.customSetup()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.centralwidget.setWhatsThis(
            _translate("MainWindow", "<html><head/><body><p>Co to jest??!!!!</p></body></html>"))
        self.label.setText(_translate("MainWindow", "ks"))
        self.label_2.setText(_translate("MainWindow", "kr"))
        self.label_3.setText(_translate("MainWindow", "gs"))
        self.label_4.setText(_translate("MainWindow", "gr"))
        self.groupBox.setTitle(_translate("MainWindow", "DB"))
        self.db_save_pbtn.setText(_translate("MainWindow", "Zapisz"))
        self.db_load_pbtn.setText(_translate("MainWindow", "Ładuj"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Plik tekstowy"))
        self.txt_save_pbtn.setText(_translate("MainWindow", "Zapisz"))
        self.txt_load_pbtn.setText(_translate("MainWindow", "Ładuj"))
        self.groupBox_2.setTitle(_translate("MainWindow", "JSON"))
        self.json_load_ptbn.setText(_translate("MainWindow", "Ładuj"))
        self.json_save_pbtn.setText(_translate("MainWindow", "Zapisz"))
        self.calculate_pbtn.setText(_translate("MainWindow", "Wykonaj obliczenia"))
        self.menuZamknij.setTitle(_translate("MainWindow", "Opcje"))
        self.actionOtw_rz.setText(_translate("MainWindow", "Otwórz"))

    def customSetup(self):
        self.ks_val_qle.setText("5")
        self.kr_val_qle.setText("5")
        self.gs_val_qle.setText("5")
        self.gr_val_qle.setText("5")

        self.calculate_pbtn.clicked.connect(self.runCalculations)

        self.calc_tab = None
        self.results_tab = None

    def runCalculations(self):
        input_vals = self.validateLimitVals()
        if len(input_vals) == 4:
            ks, kr, gs, gr = input_vals

            test_motor = Motor()
            motor_calc = MotorCalc(test_motor, limit=0, kls=ks, klr=kr, gs=gs, gr=gr)
            motor_calc.calculate()
            motor_results = MotorResults(motor_calc)

            self.results_tab = CalcResultsWidget(motor_results)
            self.results_tab.show()

            print(motor_results)
        else:
            print("Nie weszło!")

    def validateLimitVals(self) -> tuple:
        ks = int(self.ks_val_qle.text())
        kr = int(self.kr_val_qle.text())
        gs = int(self.gs_val_qle.text())
        gr = int(self.gr_val_qle.text())

        if ks <= 0:
            type(self).showErrorBox("Błędna wartość", "ks mniejsze bądź równe 0")
            return tuple()
        if kr <= 0:
            type(self).showErrorBox("Błędna wartość", "kr mniejsze bądź równe 0")
            return tuple()
        if gs <= 0:
            type(self).showErrorBox("Błędna wartość", "gs mniejsze bądź równe 0")
            return tuple()
        if gr <= 0:
            type(self).showErrorBox("Błędna wartość", "gr mniejsze bądź równe 0")
            return tuple()

        return ks, kr, gs, gr

    @staticmethod
    def showErrorBox(title: str, err_text: str):
        try:
            error_box = QMessageBox()
            error_box.setWindowTitle(title)
            error_box.setText(err_text)
            error_box.setIcon(QMessageBox.Warning)
            error_box.setStandardButtons(QMessageBox.Ok)
            x = error_box.exec_()
        except Exception as e:
            print(str(e))


if __name__ == "__main__":
    import sys

    sys.excepthook = Utils.excepthook_errormsg
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UiMainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
