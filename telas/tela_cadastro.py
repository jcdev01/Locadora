
import customtkinter as ctk
from PIL import  Image
import os
from telas.back import banco
from telas.tela_dashboard import criar_teladashboard
from telas.back.banco import cpf_existe

def criar_telacadastro(app,mudar_tela):
    frame2=ctk.CTkFrame(app)

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    img_path = os.path.join(BASE_DIR, "..", "imagens", "fundo_cadastro.png")

    fundo = ctk.CTkImage(Image.open(img_path), size=(800, 600))
    fundolabel=ctk.CTkLabel(frame2,image=fundo,text="",)
    fundolabel.place(x=0,y=0)

    texto_nome=ctk.CTkLabel(frame2,text="NOME COMPLETO",bg_color="black",text_color="white",font=("Montserrat",12,"bold"))
    texto_nome.place(x=250,y=50)


    erro_label=ctk.CTkLabel(frame2,text="",text_color="red",bg_color="black")
    erro_label.place(x=15,y=500)



    entrada_nome=ctk.CTkEntry(frame2,
                                text_color="white",
                                width=341,
                                height=40,
                                corner_radius=30,
                                border_width=2,
                                border_color="",
                                fg_color="#3a3d7b",
                                bg_color="black",)

    entrada_nome.place(x=240,y=85)

    texto_numero=ctk.CTkLabel(frame2,
                              text="NÚMERO",
                              bg_color="black",
                              text_color="white",
                              font=("Monstserrat",12,"bold"),
                              )
    texto_numero.place(x=250,y=150)

    entrada_numero=ctk.CTkEntry(frame2,
                                text_color="white",
                                width=341,
                                height=40,
                                corner_radius=30,
                                border_width=2,
                                border_color="",
                                fg_color="#3a3d7b",
                                bg_color="black",
                                placeholder_text="00 123456789")
    entrada_numero.place(x=240,y=185)

    texto_email=ctk.CTkLabel(frame2,
                             text="E-MAIL",
                             bg_color="black",
                             text_color="white",
                             font=("Monstserrat",12,"bold"))
    texto_email.place(x=250,y=250)

    entrada_email=ctk.CTkEntry (frame2,
                                text_color="white",
                                width=341,
                                height=40,
                                corner_radius=30,
                                border_width=2,
                                border_color="",
                                fg_color="#3a3d7b",
                                bg_color="black",
                                placeholder_text="nome@gmail.com")
    entrada_email.place(x=240,y=285)

    texto_cpf=ctk.CTkLabel(frame2,
                           text="CPF",
                           bg_color="black",
                           text_color="white",
                           font=("Monstserrat",12,"bold"))

    texto_cpf.place(x=250,y=350)

    entrada_cpf=ctk.CTkEntry(frame2,
                                text_color="white",
                                width=341,
                                height=40,
                                corner_radius=30,
                                border_width=2,
                                border_color="",
                                fg_color="#3a3d7b",
                                bg_color="black",
                                placeholder_text="123.456.789-00")

    entrada_cpf.place(x=240,y=385)

    texto_senha=ctk.CTkLabel(frame2,
                           text="SENHA",
                           bg_color="black",
                           text_color="white",
                           font=("Monstserrat",12,"bold"))
    texto_senha.place(x=250,y=450)

    entrada_senha_cadastro=ctk.CTkEntry(frame2,
                                text_color="white",
                                width=341,
                                height=40,
                                corner_radius=30,
                                border_width=2,
                                border_color="",
                                fg_color="#3a3d7b",
                                bg_color="black")
    entrada_senha_cadastro.place(x=240,y=485)



    def criar_conta():
        nome=entrada_nome.get()
        senha=entrada_senha_cadastro.get()
        email=entrada_email.get()
        numero=entrada_numero.get()
        cpf=entrada_cpf.get()

        if not nome or not entrada_cpf or not numero or not senha or not email or not cpf:
            erro_label.configure(text_color="red",font=("Verdana",10,"bold"),text="preencha todos os campos corretamente ")
            return
        
        elif cpf_existe(cpf):
            erro_label.configure(
                text_color="red",
                font=("Verdana", 10, "bold"),
            )
            return

        else:
            usuario = {
                "cpf":entrada_cpf.get(),
                "senha":entrada_senha_cadastro.get(),
                "email":entrada_email.get(),
                "nome":entrada_nome.get(),
                "telefone":entrada_numero.get()
            }

            banco.novoUsuario(usuario)
            banco.listar('usuarios')
            mudar_tela(criar_teladashboard)

    butao_criarconta=ctk.CTkButton(frame2,
                                text_color="white",
                                width=150,
                                height=40,
                                corner_radius=30,
                                border_width=2,
                                border_color="",
                                text="CRIAR CONTA",
                                font=("Monstserrat",10,"bold"),
                                fg_color="#3a3d7b",
                                bg_color="black",
                                command=criar_conta,
                                )
    butao_criarconta.place(x=335,y=538)


    return frame2



















