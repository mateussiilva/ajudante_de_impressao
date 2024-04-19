
from os.path import join, splitext
from PIL import Image, ImageDraw, ImageFont, ImageOps
from utils.files import listfiles
from utils.painel import get_name_painel

lenfont = 46
font = ImageFont.truetype("arial-bold.ttf", size=lenfont)

from os.path import split,splitext

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



def get_name_painel(path:str):
    _,__ = split(path)
    n,e = splitext(__)
    return n.split("-")[0].upper().strip()


def read_lines(path_file):
    with open(path_file, "r") as fp:
        data = fp.readlines

    return list(map(lambda l: l.strip("\n").strip(), data))


def main():
    Image.MAX_IMAGE_PIXELS = None  # PERIGOSO
    NOME_FILE = "paineis_nomeados.txt"
    PATH = "/media/mateus/D395-E345/TESTE DE COR"
    PATH = "images"
    p
    paineis_nomeados = read_lines(NOME_FILE)
    for file in listfiles(PATH):
        if file not in paineis_nomeados:
            nome_cliente_painel = get_name_painel(file)
            print("Escrevendo o nome no painel {}".format(nome_cliente_painel))
            with Image.open(file) as im:
                print(nome_cliente_painel)
                w, h = im.size
                print(im.size)
                if "redondo" in file.lower():
                    print("Oi")
                    new_img = ImageOps.pad(
                        im, size=(w, h), centering=(1, 1), color="white"
                    )
                    draw = ImageDraw.Draw(new_img)

                    draw.text(
                        (0, 0), nome_cliente_painel, fill="black", font=font
                    )

                    new_img.save(file)
                else:

                    new_img = ImageOps.pad(
                        im, size=(w, h+lenfont), centering=(1, 1), color="white"
                    )
                    draw = ImageDraw.Draw(new_img)

                    draw.text(
                        (0, 0), nome_cliente_painel, fill="black", font=font
                    )
                new_img.save(file)
                


if __name__ == "__main__":
    main()
