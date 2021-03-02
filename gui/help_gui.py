# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'help.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class HelpDialog(object):
    def __init__(self):
        self.Form = QtWidgets.QWidget()
        self.Form.setWindowModality(2)
        self.setupUi(self.Form)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(450, 400)
        Form.setMinimumSize(QtCore.QSize(450, 400))
        Form.setMaximumSize(QtCore.QSize(450, 400))
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 20, 803, 321))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(30, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        self.textBrowser.setMaximumSize(QtCore.QSize(400, 600))
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.ok_pbtn = QtWidgets.QPushButton(Form)
        self.ok_pbtn.setGeometry(QtCore.QRect(180, 360, 75, 23))
        self.ok_pbtn.setObjectName("ok_pbtn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.connectCustomSignals()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Pomoc"))
        self.textBrowser.setHtml(_translate("Form",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                            "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n "
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style "
                                            "type=\"text/css\">\n "
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Program został zbudowany na podstawie skryptu Matlaba obliczającego straty dodatkowe silnika indukcyjnego. Stanowił on częśc praktyczną mojej pracy magisterskiej.</p>\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Objaśnienia dot. symboli:</p>\n"
                                            "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- ks, kr, gs, gr - zmienne do określania zakresu harmonicznych, jeśli limit jest równy 0, to wtedy określają one zakres harmonicznych (ks i gs dla harmonicznych stojana, kr i gr dla harmonicznych wirnika). Gdy limit jest różny od 0, to nie mają one wpływu na obliczenia,</p>\n"
                                            "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- Ps - straty dodatkowe w zębach wirnika,</p>\n"
                                            "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- PAl - straty dodatkowe w klatce wirnika,</p>\n"
                                            "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- Pss - straty powierzchniowe w zębach stojana,</p>\n"
                                            "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- Pp - straty pulsacyjne w zębach stojana,</p>\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; "
                                            "margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Program oraz "
                                            "wcześniejszy skrypt bazują na wzorach zawartych w książce Tadeusza "
                                            "Śliwińskiego &quot;Metody obliczania silników indukcyjnych "
                                            "t.1&quot;.</p></body></html>"))
        self.ok_pbtn.setText(_translate("Form", "OK"))

    def connectCustomSignals(self):
        self.ok_pbtn.clicked.connect(self.closeDialog)

    def closeDialog(self):
        self.Form.hide()

    def show(self):
        self.Form.show()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = HelpDialog()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
