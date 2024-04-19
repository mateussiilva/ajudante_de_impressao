import os
from os.path import join, isfile


def listfiles(path: str) -> list[str]:
    try:
        l: list = []
        for data in os.listdir(path):
            p: str = join(path, data)
            if isfile(p):
                l.append(p)
    except Exception as err:
        return None
    return l
