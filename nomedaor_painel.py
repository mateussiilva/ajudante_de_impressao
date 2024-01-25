
import os

from PIL import Image, ImageDraw, ImageFont


PATH_IMAGE = "images/"
nomeimage = "ADRIANA LUISA - PAINEL REDONDO PATRULHA - 158x158 - (MALHA).jpg"
nomecliente = "ADRIANA LUISA"
pathimage = os.path.join(PATH_IMAGE, nomeimage)

lenfont = 46
fnt = ImageFont.truetype("assets/arial-bold.ttf", lenfont)

# img = Image.open(pathimage)
img = Image.new(mode="RGB", size=(600, 600),color=(255,0,255))
width, height = img.size
new_img = img.resize((width,height+lenfont))
draw = ImageDraw.Draw(new_img)

draw.text((0,height - 80), nomecliente, font=fnt, fill=(0,0, 0))
new_img.save(os.path.join(PATH_IMAGE,"teste.jpg"))
print(width,height)

