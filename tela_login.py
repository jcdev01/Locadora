import customtkinter as ctk
from PIL import Image


#configurações da tela
tela_loguin=ctk.CTk()
tela_loguin.title("Locadora")
tela_loguin.geometry("800x600")
tela_loguin.configure(fg_color="black")
tela_loguin.resizable(False,False)


#card da tela
card=ctk.CTkFrame(tela_loguin,corner_radius=15,
                  fg_color="#3a3d7b",
                  width=270,
                  height=588)
card.place(x=6,y=6)


#caminho e tamanho da imagem
fundo=ctk.CTkImage(Image.open("imagens/fundo_login.png"),
                   size=(524,589))

#carregar a imagem
label_fundo=ctk.CTkLabel(tela_loguin,image=fundo,text="")
label_fundo.place(x=290,y=6)



#texto do titulo
texto_titulo=ctk.CTkLabel(card,text="BEM VINDO! ",text_color="white",font=("Achirvo black",28,"bold"))
texto_titulo.place(x=50,y=200)

#texto subtitulo
texto_subtitulo=ctk.CTkLabel(card,text="faça seu login para continuar",text_color="white",font=("verdana",10,"bold"))
texto_subtitulo.place(x=55,y=228)


#entrada para usuário
entrada_usuario=ctk.CTkEntry(card,
                             placeholder_text="Usuario "
                             ,text_color="white"
                             ,width=250,
                             height=40,
                             corner_radius=30,
                             border_width=2,
                             border_color="",
                             fg_color="#202244")
entrada_usuario.place(x=10,y=270)


#entrada para senha
entrada_senha=ctk.CTkEntry(card,
                             placeholder_text="Senha"
                             ,text_color="white"
                             ,width=250,
                             height=40,
                             corner_radius=30,
                             border_width=2,
                             border_color="",
                             fg_color="#202244")
entrada_senha.place(x=10,y=320)


#butão pra criar conta
butao_criarconta=ctk.CTkButton(
                    card,
                    text="criar conta",
                    width=120,
                    height=35,
                    corner_radius=30,
                    border_color="",
                    fg_color="#202244")
butao_criarconta.place(x=10,y=370)


#butão para entrar
butao_entrar=ctk.CTkButton(card,
                           text="entrar",
                           width=120,
                           height=35,
                           corner_radius=30,
                           border_color="",
                           fg_color="#202244")
butao_entrar.place(x=140,y=370)


#inicia a tela
tela_loguin.mainloop()
