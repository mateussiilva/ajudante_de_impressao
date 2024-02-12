from os import listdir
from os.path import join, split, exists, isfile



def list_files(path):
    return [
        join(path,f)
        for f in listdir(path)
        if isfile(join(path,f))
    ]