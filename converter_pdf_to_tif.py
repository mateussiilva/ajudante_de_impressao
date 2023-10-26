import os
from pypdf import PdfReader
from pdf2image import convert_from_path
from PIL import Image
import colorama




def arquivo_valido(arquivo,extensões=(".tiff",".tif",".pdf")):
    """Essa função serve para validar se um arquivo tem a extensão que eu preciso
    Args:
        arquivo (str): Nome do arquivo a ser analizado
        extensões (tuple): Uma tupla onde contem as extensões que validam a condição 
    Returns:
       boll: True or False 
    """
    nome,extensao = os.path.splitext(arquivo)
    if extensao in extensões:
        return True
    return False

def converter_pdf_to_tiff(arquivo,destino):
    pdf = convert_from_path(arquivo)[0]
    try:
        p_completo = os.path.join(destino,arquivo.replace(".pdf",".tif"))
        pdf.save(p_completo)
        print(colorama.Back.GREEN, "Deu certo")
    except Exception as error:
        print("Não consegui converter sory!")
        print(colorama.Back.RED, error)

if __name__ == "__main__":
    colorama.init()
    path_origem = "arquivos_testes"
    lista_arquivos_pds = []
    
    for arquivo in os.listdir(path_origem):
        # nome, exte = os.path.splitext(arquivo)
        if arquivo_valido(arquivo):
            p_completo = os.path.join(path_origem,arquivo)
            lista_arquivos_pds.append(p_completo)
            converter_pdf_to_tiff(p_completo,"exportados")
    
        