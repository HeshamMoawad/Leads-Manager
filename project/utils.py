import pathlib
import os , datetime , re , numpy

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent

def getdir(*path)->str:
    now = datetime.datetime.now()
    directory = os.path.join(BASE_DIR,"Exports",str(now.year),str(now.month),str(now.day))
    if os.path.isdir(directory):
        return os.path.join(directory,*path)
    else :
        os.makedirs(directory)
        return os.path.join(directory,*path)


def getdirReport(*path)->str:
    now = datetime.datetime.now()
    directory = os.path.join(BASE_DIR,"Reports",str(now.year),str(now.month),str(now.day))
    if os.path.isdir(directory):
        return os.path.join(directory,*path)
    else :
        os.makedirs(directory)
        return os.path.join(directory,*path)


def increasement(array: list) -> list:
    array += [0]
    return array

def completeArray(array: list, length: int) -> list:
    while len(array) < length:
        array = increasement(array)
        if len(array) == length:
            break
    return array

    
def filterNumber(text):
    phones = re.findall(r'\+966\d{9}', text)
    if phones :
        return phones[0]
    else :
        return numpy.nan
    