import os
import glob
import sys

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


if __name__ == "_main_":
	PATH = r"\\Storage-silkart\IMPRESSAO\25 10 2023"
	main(PATH)