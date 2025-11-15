import customtkinter as ctk
from telas.tela_login import criar_telalogin
from telas.tela_cadastro import criar_telacadastro
from telas.tela_aluguel import criar_telaaluguel

# cria a janela principal
app = ctk.CTk()
app.geometry("800x600")
app.title("Locadora")
app.resizable(False, False)

# variável para guardar a tela atual
tela_atual = None

# função para trocar de tela
def mudar_tela(nova_tela):
    global tela_atual
    if tela_atual is not None:
        tela_atual.pack_forget()  # esconde a atual
    tela_atual = nova_tela(app,mudar_tela)   # cria a nova
    tela_atual.pack(fill="both", expand=True)  # mostra ela

# inicia o programa com a tela de login
mudar_tela(criar_telalogin)

app.mainloop()
