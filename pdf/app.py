
from pdf2image import convert_from_path
from PIL import Image
import os


class ManipuladorDeImagens:
    def __init__(self,caminho_arquivo:str) -> None:
        self.__path_file = caminho_arquivo
    
    
    def converter_pdf(self,extensao=".jpg"):
        p = self.__path_file
        img = convert_from_path(p, dpi=200)
        [i.save(p.replace(".pdf",extensao)) for i in img]

    

path_pdf_file = "POODLE.pdf"

manipulador = ManipuladorDeImagens(path_pdf_file)
manipulador.converter_pdf()