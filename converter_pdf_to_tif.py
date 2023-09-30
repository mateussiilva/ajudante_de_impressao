import os


path_origem = "/home/mateus/Downloads"

def arquivo_valido(arquivo,extensões=(".tiff",".tif",".pdf")):
    """Essa função serve para validar se um arquivo tem a extensão que eu preciso
    Args:
        arquivo (str): Nome do arquivo a ser analizado
        extensões (tuple): Uma tupla onde contem as extensões que validam a condição 
    Returns:
       boll: True or False 
    """
    nome,extensao = os.path.splitext(arquivo)
    if extensao in extensões:
        return True
    return False


for arquivo in os.listdir(path_origem):
    # nome, exte = os.path.splitext(arquivo)
    if arquivo_valido(arquivo):
        print(arquivo)