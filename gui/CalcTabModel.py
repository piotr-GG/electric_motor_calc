from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from model.elmag_container import ElectromagContainer


class CalcTabModel(QtCore.QAbstractTableModel):
    def __init__(self, data, horiz_header, vert_header):
        super(CalcTabModel, self).__init__()
        if issubclass(type(data), ElectromagContainer):
            self._data = data
        else:
            raise TypeError("Wrong input data for Calculation Table Model!")
        self._horiz_header = horiz_header
        self._vert_header = vert_header

    def data(self, index, role):
        if role == Qt.DisplayRole:
            if index.row() == 0:
                return str(self._data.order[index.column()])
            elif index.row() == 1:
                return str(self._data.elmag_qty[index.column()])

    def rowCount(self, index):
        return 2

    def columnCount(self, index):
        return len(self._data.order)

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = ...):
        if self._horiz_header is not None:
            if role == Qt.DisplayRole and orientation == Qt.Horizontal:
                return self._horiz_header[section]
        if self._vert_header is not None:
            if role == Qt.DisplayRole and orientation == Qt.Vertical:
                return self._vert_header[section]
