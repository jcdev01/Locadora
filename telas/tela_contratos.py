import customtkinter as ctk
from PIL import Image
import os

from telas.back.banco import contratosSalvos
from session import usuarioLogado
from telas.back.banco import escolherContrato
from main import mudar_tela


def criar_telacontrato(app,mudar_tela):
    frame5=ctk.CTkFrame(app)


    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    img_path = os.path.join(BASE_DIR, "..", "imagens", "fundo_contratos.png")

    fundo = ctk.CTkImage(Image.open(img_path), size=(800,600))

    label_fundo=ctk.CTkLabel(frame5,text="",image=fundo)
    label_fundo.place(x=0,y=0)


    texto_titulo=ctk.CTkLabel(frame5,text="CONTRATOS"
                              ,bg_color="#3a3d7b"
                              ,font=("Montserrat",24,"bold"))

    texto_titulo.place(x=60,y=30)


    contratos=contratosSalvos()


    def mostra_dados(e=None):
        valor=combo_contratos.get()

        if not valor:
            return
        id=int(valor.split(":")[1])


        contrato=escolherContrato(id)

        if contrato:
            label_carro.configure(text=f"CARRO:\n{contrato.carro}")
            label_datainicio.configure(text=f"DATA EMISSÃO:\n{contrato.dataInicio}")
            label_datafinal.configure(text=f"DATA DEVOLUÇÃO:\n{contrato.dataTermino}")
            label_valor.configure(text=f"VALOR TOTAL:\n{contrato.valor}")
            label_forma_de_pagamento.configure(text=f"FORMA DE PAGEMENTO:\n{contrato.formaPagamento}")
        else:
            print("contrato nao encontrado")



    combo_contratos = ctk.CTkComboBox(
        frame5,
        values=[f"CONTRATO:{i}" for i in contratos],
        fg_color="#4b4f9d",
        width=250,
        corner_radius=30,
        bg_color="#3a3d7b",
        border_color="#4b4f9d",
        button_color="black",
        command=mostra_dados

    )


    combo_contratos.place(x=30,y=100)






    label_datainicio=ctk.CTkLabel(frame5,text="",text_color="white",font=("Verdana",12,"bold"),bg_color="#3a3d7b")
    label_datainicio.place(x=30,y=200)

    label_datafinal=ctk.CTkLabel(frame5,text="",text_color="white",font=("Verdana",12,"bold"),bg_color="#3a3d7b")
    label_datafinal.place(x=30,y=250)

    label_carro=ctk.CTkLabel(frame5,text="",text_color="white",font=("Verdana",12,"bold"),bg_color="#3a3d7b")
    label_carro.place(x=30,y=300)

    label_valor=ctk.CTkLabel(frame5,text="",text_color="white",font=("Verdana",12,"bold"),bg_color="#3a3d7b")
    label_valor.place(x=30,y=350)

    label_forma_de_pagamento=ctk.CTkLabel(frame5,text="",text_color="white",font=("Verdana",12,"bold"),bg_color="#3a3d7b")
    label_forma_de_pagamento.place(x=30,y=400)


    def voltar():
      from telas.tela_dashboard import criar_teladashboard
      mudar_tela(criar_teladashboard)




    butao_voltar=ctk.CTkButton(frame5,
                                text_color="white",
                                width=150,
                                height=40,
                                corner_radius=20,
                                border_width=2,
                                border_color="",
                                text="VOLTAR",
                                font=("Monstserrat", 10, "bold"),
                                fg_color="#3a3d7b",
                                bg_color="#03102f"
                               ,command=voltar)
    butao_voltar.place(x=640,y=20)



    return frame5