
from pdf2image import convert_from_path
import glob
import os


def listar_arquivos(path,extensao_alvo=".tif"):
	lista_arquivos = []
	for arquivo in glob.glob(os.path.join(path,f"*{extensao_alvo}")):
		lista_arquivos.append(arquivo)

	return lista_arquivos


class ManipuladorDeImagens:
    def __init__(self) -> None:
        # self.__path_file = caminho_arquivo
        pass

    
    def converter_pdf(self,nome_arquivo,extensao=".jpg",pasta_de_destino=None):
        img = convert_from_path(nome_arquivo, dpi=1)
        if pasta_de_destino is not None:
            root,file = os.path.split(nome_arquivo)
            destino = os.path.abspath(pasta_de_destino)
            novo_arquivo = os.path.join(destino,file.replace(".pdf",extensao))
            print(novo_arquivo)
            [i.save(novo_arquivo) for i in img]
        [i.save(nome_arquivo.replace(".pdf",extensao)) for i in img]

    


manipulador = ManipuladorDeImagens()
lista_arquivos = listar_arquivos("../arquivos_testes",".pdf")
for arquivo in lista_arquivos:
    manipulador.converter_pdf(arquivo,pasta_de_destino="convertidos")