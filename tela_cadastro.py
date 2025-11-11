import customtkinter as ctk
from PIL import  Image


tela_cadastro=ctk.CTk()
tela_cadastro.geometry("800x600")
tela_cadastro.title("Locadora")
tela_cadastro.resizable(False,False)

fundo=ctk.CTkImage(Image.open("imagens/fundo_cadastro.png"),size=(800,600))
fundolabel=ctk.CTkLabel(tela_cadastro,image=fundo,text="",)
fundolabel.place(x=0,y=0)

texto_nome=ctk.CTkLabel(tela_cadastro,text="NOME COMPLETO",bg_color="black",text_color="white",font=("Montserrat",12,"bold"))
texto_nome.place(x=250,y=50)

entrada_nome=ctk.CTkEntry(tela_cadastro,
                            text_color="white",
                            width=341,
                            height=40,
                            corner_radius=30,
                            border_width=2,
                            border_color="",
                            fg_color="#3a3d7b",
                            bg_color="black")

entrada_nome.place(x=240,y=85)

texto_numero=ctk.CTkLabel(tela_cadastro,
                          text="NÚMERO",
                          bg_color="black",
                          text_color="white",
                          font=("Monstserrat",12,"bold"))
texto_numero.place(x=250,y=150)

entrada_numero=ctk.CTkEntry(tela_cadastro,
                            text_color="white",
                            width=341,
                            height=40,
                            corner_radius=30,
                            border_width=2,
                            border_color="",
                            fg_color="#3a3d7b",
                            bg_color="black")
entrada_numero.place(x=240,y=185)

texto_email=ctk.CTkLabel(tela_cadastro,
                         text="E-MAIL",
                         bg_color="black",
                         text_color="white",
                         font=("Monstserrat",12,"bold"))
texto_email.place(x=250,y=250)

entrada_email=ctk.CTkEntry (tela_cadastro,
                            text_color="white",
                            width=341,
                            height=40,
                            corner_radius=30,
                            border_width=2,
                            border_color="",
                            fg_color="#3a3d7b",
                            bg_color="black")
entrada_email.place(x=240,y=285)

texto_cpf=ctk.CTkLabel(tela_cadastro,
                       text="CPF",
                       bg_color="black",
                       text_color="white",
                       font=("Monstserrat",12,"bold"))

texto_cpf.place(x=250,y=350)

entrada_cpf=ctk.CTkEntry(tela_cadastro,
                            text_color="white",
                            width=341,
                            height=40,
                            corner_radius=30,
                            border_width=2,
                            border_color="",
                            fg_color="#3a3d7b",
                            bg_color="black")

entrada_cpf.place(x=240,y=385)

texto_senha=ctk.CTkLabel(tela_cadastro,
                       text="SENHA",
                       bg_color="black",
                       text_color="white",
                       font=("Monstserrat",12,"bold"))
texto_senha.place(x=250,y=450)

entrada_senha_cadastro=ctk.CTkEntry(tela_cadastro,
                            text_color="white",
                            width=341,
                            height=40,
                            corner_radius=30,
                            border_width=2,
                            border_color="",
                            fg_color="#3a3d7b",
                            bg_color="black")
entrada_senha_cadastro.place(x=240,y=485)

butao_criarconta=ctk.CTkButton(tela_cadastro,
                            text_color="white",
                            width=150,
                            height=40,
                            corner_radius=30,
                            border_width=2,
                            border_color="",
                            text="CRIAR CONTA",
                            font=("Monstserrat",10,"bold"),
                            fg_color="#3a3d7b",
                            bg_color="black")
butao_criarconta.place(x=335,y=538)
















tela_cadastro.mainloop()



