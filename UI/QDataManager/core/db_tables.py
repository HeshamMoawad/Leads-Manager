class Table :
    def __str__(self) -> str:
        return f"{self.__class__.__name__}"
    
    @property
    def adding_date (self):
        return self.__str__()+".adding_date"
    
    @property
    def adding_time (self):
        return self.__str__()+".adding_time"
    @property
    def all(self):
        return "*"


class SolidTables(Table):
    @property
    def id (self):
        return self.__str__()+".id"

    @property
    def deleted (self):
        return self.__str__()+".deleted"
    @property
    def active (self):
        return self.__str__()+".active"


class Sources(SolidTables):
    @property
    def source_name (self):
        return self.__str__()+".source_name"

class Agents(SolidTables):
    @property
    def agent_name (self):
        return self.__str__()+".agent_name"
    
class Projects(SolidTables):
    @property
    def project_name (self):
        return self.__str__()+".project_name"
    @property
    def extension (self):
        return self.__str__()+".extension"
    

class Data(Table):
    @property
    def number (self):
        return self.__str__()+".number"
    @property
    def source_id (self):
        return self.__str__()+".source_id"
    @property
    def name  (self):
        return self.__str__()+".name"
    @property
    def taken (self):
        return self.__str__()+".taken"
    @property
    def deleted (self):
        return self.__str__()+".deleted"
    @property
    def registered (self):
        return self.__str__()+".registered"


class Leads(Table):
    @property
    def agent_id (self):
        return self.__str__()+".agent_id"
    @property
    def number (self):
        return self.__str__()+".number"
    @property
    def name  (self):
        return self.__str__()+".name"
    @property
    def project_id (self):
        return self.__str__()+".project_id"
    @property
    def source_id (self):
        return self.__str__()+".source_id"
    @property
    def description (self):
        return self.__str__()+".description"


class Live_Data(Table):
    @property
    def agent_id (self):
        return self.__str__()+".agent_id"
    @property
    def number (self):
        return self.__str__()+".number"
    @property
    def project_id (self):
        return self.__str__()+".project_id"
    @property
    def source_id (self):
        return self.__str__()+".source_id"
