import typing
from utils import convert_tuple_to_query , only_column


class SqlConditions:
    EQUAL = " = "
    GREETER_THAN = " >= "
    LESS_THAN = " <= "
    BETWEEN =  "\nBETWEEN "
    AND = "\nAND "
    OR = " OR "

    def __query(self,operator:str,value)-> str:
        return f"{operator} '{value}'" if isinstance(value , str) else f"{operator} {value} "

    def equal(self,equals_to:str)-> str:
        return self.__query(self.EQUAL,equals_to)
        
    def between(self,between_from:str , between_to:str , operator:str = AND)-> str:
        return self.__query(self.BETWEEN,between_from) + self.__query(operator, between_to)
        
class SqlCommand:
    def __init__(self , *args) -> None:
        self.string = " ".join([str(arg) for arg in args ])
    def __str__(self) -> str:
        return f"\n{self.__class__.__name__.upper().replace('_',' ')} " + self.string
    
class Where (SqlCommand): ...

class Select(SqlCommand):
    def __init__(self,columns:typing.Union[str,typing.List[str]] , From:str ,*conditions) -> None:
        if isinstance(columns,str): super().__init__(columns,"FROM",From,"".join([str(condition) for condition in conditions ]))
        else : super().__init__(" ".join(columns),"FROM",From,"".join([str(condition) for condition in conditions ]))

class Insert_Into(SqlCommand):
    def __init__(self, table:str,columns:typing.List[str],values:typing.Union[tuple,typing.List[tuple]],*args) -> None:
        if isinstance(values,tuple): super().__init__(table,f'\n({" , ".join([only_column(col) for col in columns])})',f"\nVALUES {convert_tuple_to_query(values)}",*args)
        else : super().__init__(table,f'\n({" , ".join([only_column(col) for col in columns])})',f"\nVALUES {' ,'.join([convert_tuple_to_query(val) for val in values])}",*args)


from db_tables import *
print(Insert_Into(
    Data(),
    [Data().name,Data().adding_date],
    [("hhh",1),("hhh","dd"),]
        ))
# print(type(("hhh","dd")))