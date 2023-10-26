from pandas import DataFrame , read_sql_query
from PyQt5.QtCore import QObject
from utils import (
    replace_value_with_id ,
    merge_lists_to_dict ,
)
import sqlite3 , typing



class Table(DataFrame,QObject):

    def __init__(self,table_name:str,con:sqlite3.Connection,) -> None:
        super(Table,self).__init__()
        self.table_name = table_name
        self.con = con
        self.__dict__ = read_sql_query(f"SELECT * FROM {table_name}",con).__dict__


    def get_original(self,relations:typing.Dict[str,dict]={})-> DataFrame :
        data = self.copy()
        for column in self.columns :
            if column.endswith("_id") and column.replace("_id","") in relations.keys() :
                data[column] = data[column].map(relations[column.replace("_id","")])
        print(data)

    def get_relations(self)-> dict:
        return merge_lists_to_dict(self[self.columns[0]].to_list(),self[self.columns[1]].to_list())

    


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
t2 = Table(DATA,connection)

t2.get_original({
    SOURCES.lower() : tt.get_relations()
})
# print(tt)

