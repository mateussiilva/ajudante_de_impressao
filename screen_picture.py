from PIL import Image, ImageOps,ImageDraw
from os.path import split

p = "images/ADRIANA LUISA - PAINEL RENTANGULAR XADREX - 110x210 - (TACTEL).TIF"
with Image.open(p) as im:
    r,file = split(p)
    nome = file.split("-")[0]
    draw = ImageDraw.Draw(im)
    print(nome)
    # w,h = im.size
    
    # ImageOps.pad(im, size=(w,h+100),centering=(1,1), color="red").save("imageops_pad.png")

    # thumbnail() can also be used,
    # but will modify the image object in place