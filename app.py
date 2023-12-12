#!/usr/bin/env python3
import customtkinter as ctk

class JanelaPrincipal(ctk.CTk):
    def __init__(self,nome_janela,largura,altura):
        super().__init__()
        
        self.title(nome_janela)
        self.geometry(f"{largura}x{altura}")
    
    
    
class ContainerImagem(ctk.CTkImage):
    def __init__(self) -> None:
        super().__init__
        self.
    
if __name__ == "__main__":        
    SIZE = 720,680
    PAD_VALUE = 16
    app = JanelaPrincipal("Ajudante de Impressão",largura=SIZE[0],altura=SIZE[1])
    
    frame_arquivo = ctk.CTkFrame(app,width=SIZE[0]-10,)
    lbl_caminho = ctk.CTkLabel(frame_arquivo,text="Selecione a pasta")
    btn_abrir_imagem = ctk.CTkButton(frame_arquivo,text="Abrir Imagem")

    frame_imagem = ctk.CTkFrame(app)
    
    
    frame_arquivo.grid(pady=PAD_VALUE,padx=PAD_VALUE)
    lbl_caminho.grid(row=0,column=0,padx=PAD_VALUE)
    btn_abrir_imagem.grid(row=0,column=1,padx=PAD_VALUE)
    
    app.mainloop()
        
    
    
    
    
