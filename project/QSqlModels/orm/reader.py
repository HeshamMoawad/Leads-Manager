import pandas , typing , numpy , re
from .db import session 
from .models import RowOfData
from PyQt5.QtCore import pyqtSignal, QThread


class ReadExcelIntoDBModel(QThread):
    Faild = pyqtSignal()
    success = pyqtSignal()

    def __init__(self,filepath:str , sheetname :str = None , columnName:str='number') -> None:
        super().__init__()
        self.filepath = filepath
        self.sheetname = sheetname
        self.session = session
        self.columnName = columnName


    def run(self) -> None:
        try :
            self.data = pandas.read_excel(self.filepath,self.sheetname)
            self.data:pandas.DataFrame = self.data[list(self.data.keys())[0]]
            self.data = self.data[[self.columnName]]
            self.data.drop_duplicates(inplace=True)
            self.data.dropna(inplace=True)
            self.data[self.columnName] = self.data[self.columnName].apply(str)
            self.data[self.columnName] = self.data[self.columnName].apply(self.convertToCountryCodeStracture)
            self.data.dropna(inplace=True)
            print(self.data)
            self.data["is_exist"] = self.data[self.columnName].apply(self.checkExistValue)
            print(self.data)
            self.data = self.data[self.data['is_exist'] == False]
            print(self.data)
            self.success.emit()
        except Exception as e :
            print(e)
            self.Faild.emit()

    def apply(self,DBmodel,source_id) -> list:
        return self.data[self.columnName].apply(lambda x : DBmodel(number=x,source_id=source_id)).to_list()

    def convertToCountryCodeStracture(self,number:str):
        number = str(number)
        if number.startswith("966") :
            return f"+{number}"
        elif number.startswith("+966"):
            return number
        elif len(number) == 9 and number.startswith("5"):
            return f"+966{number}"
        else :
            return numpy.nan

    def checkExistValue(self , number:str):
        """return True if value is exist"""
        return session.query(RowOfData).filter(RowOfData.number == str(number)).first() is not None 









