from os.path import split
from PIL import Image, ImageDraw, ImageFont, ImageOps
import os

PATH_IMAGE = "images"
nomeimage = "ADRIANA LUISA - PAINEL RENTANGULAR XADREX - 110x210 - (TACTEL).TIF"
nomecliente = "ADRIANA LUISA"
pathimage = os.path.join(PATH_IMAGE, nomeimage)

lenfont = 46
font = ImageFont.truetype("assets/fonts/arial-bold.ttf", size=lenfont)


image = Image.open(pathimage)
size = image.size
w, h = size


p = "images/ADRIANA LUISA - PAINEL RENTANGULAR XADREX - 110x210 - (TACTEL).TIF"
with Image.open(p) as im:
    r, file = split(p)
    nome = file.split("-")[0]
    print(nome)
    w, h = im.size

    new_img = ImageOps.pad(
        im, size=(w, h+lenfont), centering=(1, 1), color="red"
    )
    draw = ImageDraw.Draw(new_img).text((0,0),nome,fill="black",font=font)
    
    
    new_img.save("imageops_pad.png")
