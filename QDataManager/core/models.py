from pandas import DataFrame , read_sql_query
from PyQt5.QtCore import QObject
from utils import (
    merge_lists_to_dict ,
)
import sqlite3 , typing
from PyQt5.QtSql import QSqlTableModel , QSqlQuery


class QueryModel(QSqlTableModel) :

    def __init__(self) -> None:
        super().__init__()
        self.__queryset = ""

    def get_query(self)->str:
        return self.__queryset
    
    def set_query(self,query:str) -> None:
        self.__queryset = query
        return super().setQuery(QSqlQuery(self.__queryset))
    
    def clear(self) -> None:
        self.__queryset = ""
        return super().clear()

    
class Table(DataFrame,QObject):

    def __init__(self,table_name:str,con:sqlite3.Connection,fake_relations:typing.Dict[str,dict]={},original_relations:typing.Dict[str,dict]={}) -> None:
        super(Table,self).__init__()
        self.table_name = table_name
        self.con = con
        self.fake_relations = fake_relations
        self.__dict__ = read_sql_query(f"SELECT * FROM {table_name}",con).__dict__
        self.__reverse(fake_relations) if fake_relations != {} else None


    def get_relations(self)-> dict:
        return merge_lists_to_dict(self[self.columns[0]].to_list(),self[self.columns[1]].to_list())

    def __reverse(self,relations:typing.Dict[str,dict])-> None :
        for column in self.columns :
            col_formatter = f"""{column.replace("_id","")}s"""
            if column.endswith("_id") and col_formatter in relations.keys() :
                self[column] = self[column].map(relations[col_formatter])
                

class DataReader(QObject):
    
    def __init__(self,db_path:str="Data\database.db") -> None:
        super().__init__()
        self.connection = sqlite3.connect(db_path)
    
    @property 
    def Sources(self)-> DataFrame: 
        return read_sql_query(
            """
            SELECT * FROM Sources ;
            """,
            con = self.connection
        )
    
    @property 
    def Agents(self)-> DataFrame: 
        return read_sql_query(
            """
            SELECT * FROM Agents ;
            """,
            con = self.connection
        )
    
    @property 
    def Projects(self)-> DataFrame: 
        return read_sql_query(
            """
            SELECT * FROM Projects ;
            """,
            con = self.connection
        )

    @property 
    def Data(self)-> DataFrame: 
        return read_sql_query(
            """
            SELECT * 
            FROM Data 
            JOIN Sources on Data.source_id = Sources.source_name
            """ ,
            con = self.connection
        )

    @property 
    def Live_Data(self)-> DataFrame: 
        return read_sql_query(
            """
            SELECT * 
            FROM Live_Data 
            JOIN Sources on Live_Data.source_id = Sources.source_name
            JOIN Agents  on Live_Data.agent_id = Agents.agent_name
            JOIN Projects on Live_Data.project_id = Projects.project_name
            """ ,
            con = self.connection
        )

    @property 
    def Leads(self)-> DataFrame: 
        return read_sql_query(
            """
            SELECT * 
            FROM Leads 
            JOIN Sources on Leads.source_id = Sources.source_name
            JOIN Agents  on Leads.agent_id = Agents.agent_name
            JOIN Projects on Leads.project_id = Projects.project_name
            """ ,
            con = self.connection
        )

from _constants import LIVE_DATA , AGENTS , SOURCES , PROJECTS , DATA

connection = sqlite3.connect("Data\database.db")

tt = Table(SOURCES,connection)
t2 = Table(DATA,connection,fake_relations={
    SOURCES.lower() : tt.get_relations()
})
print(tt)

# t2.set_original()
print(t2)

