#tela pra alugar os carros
import customtkinter as ctk
from PIL import Image
import os


def criar_telaaluguel(app, mudar_tela,):

    frame = ctk.CTkFrame(app, fg_color="#3a3d7b")

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    img_path = os.path.join(BASE_DIR, "..", "imagens", "fundo_aluguel.png")

    fundo = ctk.CTkImage(Image.open(img_path), size=(800, 600))
    fundo_label = ctk.CTkLabel(frame, image=fundo, text="")
    fundo_label.place(x=0, y=0)

    def voltar():
        from Locadora.telas.tela_dashboard import criar_teladashboard
        mudar_tela(criar_teladashboard)


    botao_voltar = ctk.CTkButton(
        frame,
        text= "VOLTAR",
        fg_color= "#202244",
        width= 100,
        height= 32,
        corner_radius= 20,
        command= voltar,
        bg_color= "black"
    )
    botao_voltar.place(x=680, y=20)

    base_y = 140   # ajustar

    # Retirada
    titulo_retirada = ctk.CTkLabel(
        frame, text="Retirada",
        text_color="white",
        font=("Montserrat", 18, "italic", "bold"),
        bg_color="#3a3d7b"
    )
    titulo_retirada.place(x=50, y=base_y)

    data_retirada = ctk.CTkEntry(
        frame,
        width= 200,
        placeholder_text= "Data (DD/MM/AAAA)",
        text_color="black",
        fg_color="white",
        corner_radius=30,
        border_color="#3a3d7b"
    )
    data_retirada.place(x=50, y=base_y + 30)

    # Devolução
    titulo_devolucao = ctk.CTkLabel(
        frame, text= "Devolução",
        text_color= "white",
        font=("Montserrat", 18, "italic", "bold"),
        bg_color= "#3a3d7b"

    )
    titulo_devolucao.place(x=50, y=base_y + 110)

    data_devolucao = ctk.CTkEntry(
        frame, width=200,
        placeholder_text="Data (DD/MM/AAAA)",
        text_color="black",
        fg_color="white",
        corner_radius=30,
        border_color="#3a3d7b"
    )
    data_devolucao.place(x=50, y=base_y + 140)

    # Valor total
    titulo_valor = ctk.CTkLabel(
        frame,
        text="Cálculo do valor total:",
        text_color="white",
        font=("Montserrat", 18, "italic", "bold"),
        bg_color="#3a3d7b"
    )
    titulo_valor.place(x=50, y=base_y + 210)

    valor_label = ctk.CTkLabel(
        frame,
        text="R$ 0,00",
        text_color="white",
        font=("Montserrat", 16, "bold"),
        fg_color = "#202244",
        bg_color="#3a3d7b",  
        corner_radius = 20,
    )
    valor_label.place(x=50, y=base_y + 240)

    # forma de pagamento
    titulo_pagamento = ctk.CTkLabel(
        frame,
        text="Forma de pagamento:",
        text_color="white",
        font=("Montserrat", 18, "italic", "bold"),
        bg_color="#3a3d7b"
    )
    titulo_pagamento.place(x=50, y=base_y + 300)

    pagamento_combo = ctk.CTkComboBox(
        frame,
        values=["Crédito", "Débito", "Pix", "Dinheiro"],
        width=200,
        fg_color="white",
        corner_radius=30,
        border_color="#3a3d7b",
        text_color="black"
    )
    pagamento_combo.place(x=50, y=base_y + 340)

    # Gerar contrato
    def gerar_contrato():
        print("=== CONTRATO GERADO ===")
        print("Retirada:", data_retirada.get())
        print("Devolução:", data_devolucao.get())
        print("Pagamento:", pagamento_combo.get())
        mudar_tela(criar_teladashboard)

    botao_contrato = ctk.CTkButton(
        frame,
        text = "GERAR CONTRATO",
        fg_color = "#202244",
        bg_color="#3a3d7b",  
        width = 180,
        height = 40,
        corner_radius = 20,
        command = gerar_contrato
    )
    botao_contrato.place(x = 280, y = base_y + 330)

    return frame
