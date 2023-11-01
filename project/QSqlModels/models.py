from PyQt5.QtCore import QAbstractListModel , QModelIndex , Qt
from .orm import (
    session , 
    Agent
)





class ListModel(QAbstractListModel):

    def __init__(self , ListedORMModel:Agent) -> None:
        super().__init__()
        self.session = session
        self.ListedORMModel = ListedORMModel
        self.rows = self.session.query(self.ListedORMModel).filter(self.ListedORMModel.deleted == 0 , self.ListedORMModel.active == 1).all()

    
    def rowCount(self, parent=QModelIndex()):
        return len(self.rows)

    def refresh(self):
        self.rows = self.session.query(self.ListedORMModel).filter(self.ListedORMModel.deleted == 0 , self.ListedORMModel.active == 1).all()

    def data(self, index: QModelIndex, role: int = ...):
        if role == Qt.ItemDataRole.DisplayRole :
            return self.rows[index.row()].name










