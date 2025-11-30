#tela do dashboard
import customtkinter as ctk
from PIL import Image
import  os
from telas.tela_aluguel import criar_telaaluguel
from telas.back.classes import *
from telas.back.banco import escolherCarro
import Locadora.session
from Locadora.telas.back.classes import Carro


def criar_teladashboard(app, mudar_tela):
    frame4 = ctk.CTkFrame(app, fg_color="black")
    usuario=Locadora.session.usuarioLogado

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    img_path_fundo = os.path.join(BASE_DIR, "..", "imagens", "fundo_dashboard.png")

    imagem_fundo =ctk.CTkImage(Image.open(img_path_fundo),size=(800,600))

    label_fundo=ctk.CTkLabel(frame4,text="",image=imagem_fundo)
    label_fundo.place(x=0,y=0)

    def alugar():
       mudar_tela(criar_telaaluguel)


    botao_onix=ctk.CTkButton(frame4,
                             text="reservar",
                             fg_color="#202244",
                             width=100,
                             height=25,
                             border_color="",
                             corner_radius=20,
                             command=lambda: (escolherCarro('AAA1111'), alugar()),
                             bg_color="#3a3d7b",
                             )

    botao_onix.place(x=225,y=90)



    botao_onix_sedan=ctk.CTkButton(frame4,
                             text="reservar",
                             fg_color="#202244",
                             width=100,
                             height=25,
                             border_color="",
                             corner_radius=20,
                             command=lambda: (escolherCarro('BBB2222'), alugar()),
                             bg_color="#3a3d7b")

    botao_onix_sedan.place(x=225,y=240)



    botao_mobi=ctk.CTkButton(frame4,
                             text="reservar",
                             fg_color="#202244",
                             width=100,
                             height=25,
                             border_color="",
                             corner_radius=20,
                             command=lambda: (escolherCarro('CCC3333'), alugar()),
                             bg_color="#3a3d7b")

    botao_mobi.place(x=225,y=390)



    botao_kwid=ctk.CTkButton(frame4,
                             text="reservar",
                             fg_color="#202244",
                             width=100,
                             height=25,
                             border_color="",
                             corner_radius=20,
                             command=lambda: (escolherCarro('DDD4444'), alugar()),
                             bg_color="#3a3d7b"
                             )
    botao_kwid.place(x=490,y=85)



    botao_civic=ctk.CTkButton(frame4,
                             text="reservar",
                             fg_color="#202244",
                             width=100,
                             height=25,
                             border_color="",
                             corner_radius=20,
                             command=lambda: (escolherCarro('EEE5555'), alugar()),
                             bg_color="#3a3d7b",
                                )
    botao_civic.place(x=490,y=240)



    botao_tracker=ctk.CTkButton(frame4,
                                text="reservar",
                                fg_color="#202244",
                                width=100,
                                height=25,
                                border_color="",
                                corner_radius=20,
                                bg_color="#3a3d7b",
                                command=lambda: (escolherCarro('FFF6666'), alugar())
                             )
    botao_tracker.place(x=490,y=390)


    def selecionar_carro():
        Locadora.session.carroEscolhido=Carro



    botao_reservars=ctk.CTkButton(frame4,
                                  text="ver minhas reservas",
                                  height=30,
                                  width=135,
                                  fg_color="#3a3d7b",
                                  bg_color="#4b4f9d",
                                  corner_radius=50
                                  )
    botao_reservars.place(x=40,y=433)

    label_dados = ctk.CTkLabel(frame4, text="seus dados",
                               text_color="white",
                               fg_color="#4b4f9d",
                               font=("Poppins", 16, "bold"))
    label_dados.place(x=59, y=163)

    usuario_nome=ctk.CTkLabel(frame4,text=f"Número:\n{usuario.nome}",
                              font=("Poppins",10,"bold"),
                              text_color="white",
                              bg_color="#3a3d7b")
    usuario_nome.place(x=40,y=210)

    usuario_numero=ctk.CTkLabel(frame4,text=f"Número:\n{usuario.telefone}",
                                font=("Poppins", 10, "bold"),
                                text_color="white",
                                bg_color="#3a3d7b")
    usuario_numero.place(x=40,y=250)

    usuario_cpf=ctk.CTkLabel(frame4,text=f"CPF:\n{usuario.cpf}",
                                font=("Poppins", 10, "bold"),
                                text_color="white",
                                bg_color="#3a3d7b")
    usuario_cpf.place(x=40,y=290)

    usuario_email=ctk.CTkLabel(frame4,text=f"Email:\n{usuario.email}",
                               font=("Poppins", 10, "bold"),
                               text_color="white",
                               bg_color="#3a3d7b"
                               )
    usuario_email.place(x=40,y=330)






    return frame4

