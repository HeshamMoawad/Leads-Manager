from PyQt5.QtCore import QAbstractTableModel, QAbstractListModel , QModelIndex , Qt , QThread
from .orm import (
    session , 
    Agent ,
    RowOfData ,
    Source
)
import typing
from PyQt5.QtSql import QSqlTableModel , QSqlQuery , QSqlDatabase
from PyQt5 import QtCore , QtWidgets


class ListModel(QAbstractListModel):

    def __init__(self , ListedORMModel) -> None:
        super().__init__()
        self.session = session
        self.ListedORMModel = ListedORMModel
        self.rows = self.session.query(self.ListedORMModel).filter(self.ListedORMModel.deleted == 0 , self.ListedORMModel.active == 1).all()

    
    def rowCount(self, parent=QModelIndex()):
        return len(self.rows)

    def refresh(self):
        self.clear()
        self.rows = self.session.query(self.ListedORMModel).filter(self.ListedORMModel.deleted == 0 , self.ListedORMModel.active == 1).all()

    def data(self, index: QModelIndex, role: int = ...):
        if role == Qt.ItemDataRole.DisplayRole :
            return self.rows[index.row()].name

    def clear(self):
        self.beginRemoveRows(QModelIndex(),0,self.rowCount())
        self.rows.clear()
        self.endRemoveRows()




class TableModelView(QSqlTableModel):
    def __init__(self ,table:str , parent=None) -> None:
        super().__init__(parent)
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("Data\database.db")
        db.open()
        # query = str(session.query(RowOfData,Source.name).join(Source,RowOfData.source_id == Source.id ))
        # print(query)
        self.setQuery(QSqlQuery(f"SELECT * FROM {table}"))
        self.select()
        db.close()


    def flags(self, index: QtCore.QModelIndex) -> QtCore.Qt.ItemFlags:
        return super().flags(index) & ~Qt.ItemFlag.ItemIsEditable




