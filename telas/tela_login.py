import customtkinter as ctk
from PIL import Image
from Locadora.banco import login
import os
from Locadora.telas.tela_cadastro import criar_telacadastro
from Locadora.telas.tela_dashboard import criar_teladashboard

# configurações da tela
def criar_telalogin(app, mudar_tela):
    frame1 = ctk.CTkFrame(app,fg_color="black")

    # card da tela
    card = ctk.CTkFrame(frame1,
                        corner_radius=15,
                        fg_color="#3a3d7b",
                        width=270,
                        height=588)
    card.place(x=6, y=6)

    # imagem de fundo
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    img_path = os.path.join(BASE_DIR, "..", "imagens", "fundo_login.png")

    fundo = ctk.CTkImage(Image.open(img_path), size=(524, 589))
    
    label_fundo = ctk.CTkLabel(frame1,
                               image=fundo,
                               text="")
    label_fundo.place(x=290, y=6)

    # textos
    texto_titulo = ctk.CTkLabel(frame1, text="BEM VINDO!",
                                text_color="white",
                                font=("Archivo Black", 28, "bold"),
                                fg_color="#3a3d7b")
    texto_titulo.place(x=50, y=200)

    texto_subtitulo = ctk.CTkLabel(card,
                                   text="faça seu login para continuar",
                                   text_color="white",
                                   font=("verdana", 10, "bold"))
    texto_subtitulo.place(x=55, y=228)

    erro_label = ctk.CTkLabel(card,
                              text="",
                              text_color="red",
                              bg_color="#3a3d7b",
                              font=("Verdana", 10, "bold"))
    erro_label.place(x=50, y=250)

    # entradas
    entrada_login = ctk.CTkEntry(card,
                                   placeholder_text="Login",
                                   text_color="white",
                                   width=250,
                                   height=40,
                                   corner_radius=30,
                                   fg_color="#202244",
                                   border_color="#202244")
    entrada_login.place(x=10, y=270)

    entrada_senha = ctk.CTkEntry(card,
                                 placeholder_text="Senha",
                                 text_color="white",
                                 width=250,
                                 height=40,
                                 corner_radius=30,
                                 fg_color="#202244",
                                 border_color="#202244")
    entrada_senha.place(x=10, y=320)

    # botão criar conta → troca de tela
    butao_criarconta = ctk.CTkButton(
        card,
        text="Criar conta",
        width=120,
        height=35,
        corner_radius=30,
        fg_color="#202244",
        command=lambda: mudar_tela(criar_telacadastro)
    )
    butao_criarconta.place(x=10, y=370)

    erro_label.place(x=50,y=250)
    # função de login
    def tenta_login():
        usuario = entrada_login.get()
        senha = entrada_senha.get()
        if not entrada_login.get() or  not entrada_senha.get():
            erro_label.configure(text="preencha todas os campos",text_color="red")
            return


        if login(usuario, senha):
            print("Login realizado com sucesso")
            mudar_tela(criar_teladashboard)
        else:
            erro_label.configure(text="Usuário ou senha incorretos", text_color="red")

    # botão entrar
    butao_entrar = ctk.CTkButton(card, text="Entrar", width=120, height=35,
                                 corner_radius=30, fg_color="#202244", command=tenta_login,

                                 )
    butao_entrar.place(x=140, y=370)

    return frame1
