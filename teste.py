# from PySimpleGUI import Window,WIN_CLOSED,Text,InputCombo


matrixdados = [
    [",ateus","teste","ttttttttt"]
]

matrix = [
    ["Tacte", "23.54", "19"],
    ["Malha", "23.54", "19"],
    ["Malha", "23.54", "19"],
    ["Malha", "23.54", "19"],
    ["Malha", "23.54", "19"],
    ["Malha", "23.54", "19"],
    ["Malha", "23.54", "19"],
]
def update_tabela(dados, matrix: list[list]):
    linha = dados
    # for linha in matrix:
    matrix.insert(len(matrix),linha)
    return matrix

for linha in matrix:
    matrixdados.insert(len(matrixdados),linha)

print(matrixdados)