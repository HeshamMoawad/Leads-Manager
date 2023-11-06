import pathlib
import os , datetime

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent

def getdir(*path)->str:
    now = datetime.datetime.now()
    directory = os.path.join(BASE_DIR,"Exports",str(now.year),str(now.month),str(now.day))
    if os.path.isdir(directory):
        return os.path.join(directory,*path)
    else :
        os.makedirs(directory)
        return os.path.join(directory,*path)


