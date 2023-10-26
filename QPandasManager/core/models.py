from pandas import DataFrame , read_sql_query
from PyQt5.QtCore import QObject
import sqlite3



class Table(DataFrame):

    def __init__(self) -> None:
        super().__init__()

    




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

