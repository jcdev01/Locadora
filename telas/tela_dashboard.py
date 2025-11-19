#tela do dashbord
import customtkinter as ctk
from PIL import Image
import  os
from Locadora.telas.tela_aluguel import criar_telaaluguel


def criar_teladashboard(app,mudar_tela):
    frame4 = ctk.CTkFrame(app, fg_color="black")

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
                             command=alugar
                             )

    botao_onix.place(x=225,y=90)



    botao_onix_sedan=ctk.CTkButton(frame4,
                             text="reservar",
                             fg_color="#202244",
                             width=100,
                             height=25,
                             border_color="",
                             corner_radius=20,
                             command=alugar)

    botao_onix_sedan.place(x=225,y=240)



    botao_mobi=ctk.CTkButton(frame4,
                             text="reservar",
                             fg_color="#202244",
                             width=100,
                             height=25,
                             border_color="",
                             corner_radius=20,
                             command=alugar)

    botao_mobi.place(x=225,y=390)



    botao_kwid=ctk.CTkButton(frame4,
                             text="reservar",
                             fg_color="#202244",
                             width=100,
                             height=25,
                             border_color="",
                             corner_radius=20,
                             command=alugar
                             )
    botao_kwid.place(x=490,y=85)



    botao_civic=ctk.CTkButton(frame4,
                             text="reservar",
                             fg_color="#202244",
                             width=100,
                             height=25,
                             border_color="",
                             corner_radius=20,
                              command=alugar
                             )
    botao_civic.place(x=490,y=240)



    botao_tracker=ctk.CTkButton(frame4,
                                text="reservar",
                                fg_color="#202244",
                                width=100,
                                height=25,
                                border_color="",
                                corner_radius=20,
                                command=alugar
                             )
    botao_tracker.place(x=490,y=390)






    botao_reservars=ctk.CTkButton(frame4,text="ver minhas reservas",height=30,width=135,fg_color="#3a3d7b",
                                  )
    botao_reservars.place(x=40,y=433)

    label_titulo = ctk.CTkLabel(frame4,
                                text="CONCHEÇA NOSSA FROTA",
                                text_color="white",
                                font=("Poppins", 30, "bold"))

    label_titulo.place(x=270, y=15)

    label_dados = ctk.CTkLabel(frame4, text="seus dados",
                               text_color="white",
                               fg_color="#4b4f9d",
                               font=("Poppins", 16, "bold"))
    label_dados.place(x=59, y=163)

    return frame4

