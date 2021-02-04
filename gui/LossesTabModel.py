from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from losses import Losses


class LossesTabModel(QtCore.QAbstractTableModel):
    def __init__(self, data, vert_header):
        super(LossesTabModel, self).__init__()
        if isinstance(data, tuple) and isinstance(data[0], Losses) and isinstance(data[1], Losses):
            self._losses_1 = data[0]
            self._losses_2 = data[1]
        else:
            raise TypeError("Wrong input data for Losses Table Model!")
        self._vert_header = vert_header

    def data(self, index, role):
        if role == Qt.DisplayRole:
            if index.row() == 0:
                return str(self._losses_1.order[index.column()])
            elif index.row() == 1:
                return str(self._losses_1.losses[index.column()])
            elif index.row() == 2:
                return str(self._losses_2.losses[index.column()])

    def rowCount(self, index):
        return 3

    def columnCount(self, index):
        return len(self._losses_1.order)

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = ...):
        if self._vert_header is not None:
            if role == Qt.DisplayRole and orientation == Qt.Vertical:
                return self._vert_header[section]
