

def merge_lists_to_dict(keys_list:list,values_list:list):
    return {keys_list[i]: values_list[i] for i in range(len(keys_list))}

def convert_str_to_query(string):
    if isinstance(string,str):
        return f"'{string}'"
    else :
        return str(string)
    
def convert_tuple_to_query(tuple:tuple):
    return f"\n({','.join([convert_str_to_query(val) for val in tuple])})"

def only_column(string:str):
    return string.split(".")[-1]


