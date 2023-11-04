import pandas , typing
from .db import session



class ReadExcelIntoDBModel:


    def __init__(self,filepath:str , sheetname :str = None , columnName:str='number') -> None:
        self.filepath = filepath
        self.sheetname = sheetname
        self.session = session
        self.data = pandas.read_excel(filepath,sheetname)
        self.data:pandas.DataFrame = self.data[list(self.data.keys())[0]]
        self.data.drop_duplicates(inplace=True)
        self.data.dropna(inplace=True)
        self.columnName = columnName
        

    def apply(self,DBmodel,source_id) -> list:
        return self.data[list(self.data.columns)[0]].apply(lambda x : DBmodel(number=x,source_id=source_id)).to_list()

    def columns(self):
        return [str(column).lower() for column in list(self.data.columns) ]

    def validate(self):
        return self.columnName in self.columns()











