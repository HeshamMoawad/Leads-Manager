from PyQt5.QtCore import QAbstractTableModel , pyqtSignal , QModelIndex , Qt 

import pandas , typing


class TableModelView(QAbstractTableModel):
    lengthChanged = pyqtSignal(int)
    message = pyqtSignal(str)
    def __init__(self, columns:typing.List[str]):
        super().__init__()
        self._data = pandas.DataFrame(columns=columns) 

    @property
    def columns(self):
        return self._data.columns

    def rowCount(self,parent: QModelIndex = ...):
        return len(self._data)

    def columnCount(self,parent: QModelIndex = ... ):
        return len(self._data.columns)


    def data(self, index, role):
        if role == Qt.DisplayRole:
            return str(self._data.loc[index.row()][index.column()])
        return None

    def flags(self, index: QModelIndex) -> Qt.ItemFlags:
        return Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled
    
    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal and section < len(self._data.columns):
                return self._data.columns[section]
            elif orientation == Qt.Vertical:
                return str(section + 1)
        return None


    def dataframe(self)->pandas.DataFrame:
        return self._data

    def clear(self):
        self.beginResetModel()
        self._data = pandas.DataFrame(columns=self._data.columns)
        self.lengthChanged.emit(self.rowCount())
        self.endResetModel()
        

    def updateDataFrame(self,df:pandas.DataFrame):
        self.beginInsertRows(QModelIndex(), len(self._data), len(self._data) + len(df))
        self._data = pandas.concat([self._data,df])
        self.lengthChanged.emit(self.rowCount())
        self.endInsertRows()


    def addrow(self, row):
        self.beginInsertRows(QModelIndex(), len(self._data), len(self._data))
        self._data.loc[len(self._data)] = row
        self.lengthChanged.emit(self.rowCount())
        self.endInsertRows()

    def export(self):
        try :
            name = f"Export.xlsx"
            self._data.to_excel(name,index=False)
            self.message.emit(f"Exported Successfully as {name}")
        except :
            self.message.emit("Can't Export sheet ")
