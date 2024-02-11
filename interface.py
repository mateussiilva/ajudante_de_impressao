
import sys

from PySimpleGUI import (
    Window, Text, Table, WIN_CLOSED,
    FolderBrowse, Button, Input, Multiline
)

from utils.files import list_files


def create_table(headers: list[str], values: list, size: tuple):
    return [
        [Table(values=values, headings=headers, num_rows=True,
               enable_click_events=True, enable_events=True,
               size=size, expand_x=True, expand_y=True
               )]
    ]


layout = [
    [Text("Direotrio:"), Input(key="-PATH-"), FolderBrowse("GetFolder"),
     Button("ListFiles", k="-LIST_FILES-")],
    [Multiline("", key="-RES-")]

]


def mainloop(window):
    while 1:
        events, values = window.read()
        if events == "-LIST_FILES-":
            p = values["-PATH-"]
            arquivos = list_files(p)
            for arquivo in arquivos:

                print(arquivo)
        if events == WIN_CLOSED:
            break
        else:
            print(events)
    window.close()
    sys.exit(0)


if __name__ == "__main__":
    SIZE = (700, 600)
    window = Window("Ajudante de Impressão", layout, size=SIZE)
    mainloop(window=window)
