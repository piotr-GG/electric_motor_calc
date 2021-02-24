from PyQt5.QtWidgets import QWidget, QProgressBar, QVBoxLayout


class ProgressBar(QWidget):
    def __init__(self):
        super(ProgressBar, self).__init__()
        self.setWindowTitle("Obliczenia w toku")
        self.pbar = QProgressBar(self)
        self.pbar.setValue(0)
        self.resize(300, 100)
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.pbar)
        self.setLayout(self.vbox)

        self.finished = False

    # def show(self):
    #     self.show()

    def signal_accept(self, val):
        val = int(val)
        self.pbar.setValue(val)
        print("Odebrano wartość", val)
        if val == 100:
            self.finished = True
            self.hide()
            print("Rzekomy koniec")

