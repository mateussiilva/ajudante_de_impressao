from os.path import split,splitext




def get_name_painel(path:str):
    _,__ = split(path)
    n,e = splitext(__)
    return n.split("-")[0].upper().strip()
