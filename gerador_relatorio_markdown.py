from os.path import join, isfile
from os import listdir

def lerlinhasarquivo(filename):
    with open(filename,"r+") as fp:
        lines = fp.readlines()

    return lines

RELATORIO = r"arquivos_testes/relatorio.txt"
textoteste = "RETIRADA PELA MANHÃ:"
arquivoinicial = lerlinhasarquivo(RELATORIO)
print(type(arquivoinicial))
# print(arquivoinicial)
for linha in arquivoinicial:
    if len(linha) > 0:
        utlchar = linha[-2]
        if  utlchar == ":":
            print(linha)

