import os
import glob
import sys
from PIL import Image
Image.MAX_IMAGE_PIXELS = None



def pixel_for_cm(size,dpi):
	if len(size) == 2:
		return tuple(map(lambda x: 2.54 * (x / dpi),size))


def get_size_image_and_dpi(path_file):
	try:
		i = Image.open(path_file)
		return i.size,int(i.info["dpi"][0])
	except FileNotFoundError:
		print(f"O arquivo '{path_file}' não exite")
	except Exception as err:
		print(err)


def listar_arquivos(path,extensao_alvo=".tif"):
	lista_arquivos = []
	for arquivo in glob.glob(os.path.join(path,f"*{extensao_alvo}")):
		lista_arquivos.append(arquivo)

	return lista_arquivos

metros_linear_malha = metros_linear_tactel = 0
def main(path):
	soma = 0
	arquivos = listar_arquivos(path)
	if len(arquivos) > 0:
		for arquivo in arquivos:
			dimensoes,dpi = get_size_image_and_dpi(arquivo)
			metro_linear = pixel_for_cm(dimensoes,dpi)[0]
			soma += metro_linear
			# print(metro_linear)
		print(soma)


if _name_ == "_main_":
	PATH = r"\\Storage-silkart\IMPRESSAO\25 10 2023"
	main(PATH)