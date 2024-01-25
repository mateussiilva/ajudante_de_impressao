
""" 

Sistema de controle de estoque de tecido 

- [ ] Tactel

"""

from PySimpleGUI import Window, WIN_CLOSED, Text, Combo, Button, Table, Frame,InputCombo

TIPOS_TECIDOS = ("Tactel Vipal", "Tactel Alexandre", "Malha", "Crepe Salinas")
SIZE = 640, 600
headers = ["Tecido", "Metragem", "Data"]
matrixdados = [
    ["Tactel Vipal", "100.50", "18/01/2024"]
]


TABELA_TECIDO = [
    [Table(
        values=matrixdados, headings=headers,
        key="-TABELA_TECIDO-", auto_size_columns=False,
        expand_x=True, expand_y=True,
        justification="center", enable_click_events=True,
        enable_events=True)]

]

TIPOS_PRODUÇÃO = ["Otimimzação Malha", "Otimimzação Tactel", "Das minys SEDA"]
FRAME_PRODUÇÃO = [
    [Text("Tipo"), Combo(values=TIPOS_PRODUÇÃO,
                         key="-PRODUCAO-"), Text("Metros:"),InputCombo(values=[],size=(10,1),key="-METRAGEM-")],
    [Button("Produzir", key="-PRODUZIR-")]
]

layout = [
    # [Text("Tecido"), Combo(values=TIPOS_TECIDOS, key="-TECIDO-")],
    [Frame("Tecidos", TABELA_TECIDO, size=(640, 150))],
    [Frame("Produção", layout=FRAME_PRODUÇÃO, size=(640, 150))],
    [Button("Refresh Table", key="-REFRESH_TABLE-")],
]


window = Window("Estoque", layout, size=SIZE)


def update_tabela(dados, matrix: list[list]):
    linha = dados
    # for linha in matrix:
    matrix.insert(len(matrix), linha)
    return matrix


while 1:
    events, values = window.read()
    tabela = values["-TABELA_TECIDO-"] if values["-TABELA_TECIDO-"] is not None else None

    if events == "-PRODUZIR-":
        metragemtecido = matrixdados[tabela[0]] if len(
            tabela) < 2 else matrixdados[tabela[0]:len(tabela)-1]
        metragemtecido: float = float(metragemtecido[1])
        metrosproducao = float(values["-METRAGEM-"]) 
        print(f"Você tem {metragemtecido - metrosproducao}m")

    if events == "-REFRESH_TABLE-":
        window.refresh()

    if events == WIN_CLOSED:
        break


window.close()
