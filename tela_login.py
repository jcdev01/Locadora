#tela de login
import customtkinter as ctk



tela_loguin=ctk.CTk()
tela_loguin.title("Locadora")
tela_loguin.geometry("800x600")
tela_loguin.configure(fg_color="#1e1b3a")
tela_loguin.resizable(False,False)

texto_titulo=ctk.CTkLabel(tela_loguin,text="Locadora",text_color="white",font=("Verdana",40,"bold"))
texto_titulo.place(x=350,y=150)

texto_subtitulo=ctk.CTkLabel(tela_loguin,text="Bem vindo",text_color="white",font=("verdana",44,"bold"))
texto_subtitulo.place(x=300,y=250)

entrada_usuario=ctk.CTkEntry(tela_loguin,
                             placeholder_text="Usuario "
                             ,text_color="white"
                             ,width=250,
                             height=40,
                             corner_radius=10,
                             border_width=2,
                             border_color="#8b5cf6",
                             fg_color="#1e1b3a")

entrada_usuario.place(x=300,y=350)

butao_criarconta=ctk.CTkButton(
                    tela_loguin,
                    text="criar conta",
                    width=120,
                    height=35,
                    corner_radius=10,
                    border_color="#8b5cf6",
                    fg_color="#3b3570")
butao_criarconta.place(x=300,y=410)

butao_entrar=ctk.CTkButton(tela_loguin,
                           text="entrar",
                           width=120,
                           height=35,
                           corner_radius=10,
                           border_color="#8b5cf6",
                           fg_color="#3b3570")
butao_entrar.place(x=427,y=410)




tela_loguin.mainloop()
