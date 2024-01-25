from os.path import join, isfile
from os import listdir

def lerlinhasarquivo(filename):
    with open(filename,"r+") as fp:
        lines = fp.readlines()

    return lines

RELATORIO = r"arquivos_testes/relatorio.txt"
textoteste = "RETIRADA PELA MANHÃ:"
arquivoinicial = lerlinhasarquivo(RELATORIO)
arquivo = open("relatorio.md","w+")
print(type(arquivoinicial))
# print(arquivoinicial)
for linha in arquivoinicial:
    try:
        utlchar = linha[-2] if len(linha) > 0 else None
    except:
        pass
    if  utlchar == ":":
        newline = f"## {linha}\n"
        arquivo.write(newline)
    elif len(linha) > 0:
        newline = f"- [ ] {linha}\n"
        arquivo.write(newline)
arquivo.close()
