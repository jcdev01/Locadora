import customtkinter as ctk
from PIL import Image
import os


frame5=ctk.CTk()
frame5.geometry("800x600")
frame5.title("tela contratos")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(BASE_DIR, "..", "imagens", "fundo_contratos.png")

fundo = ctk.CTkImage(Image.open(img_path), size=(800,600))

label_fundo=ctk.CTkLabel(frame5,text="",image=fundo)
label_fundo.place(x=0,y=0)


texto_titulo=ctk.CTkLabel(frame5,text="CONTRATOS"
                          ,bg_color="#3a3d7b"
                          ,font=("Montserrat",24,"bold"))

texto_titulo.place(x=60,y=30)



combo_contratos=ctk.CTkComboBox(frame5,fg_color="#4b4f9d",
                                width=250,
                                corner_radius=30,
                                bg_color="#3a3d7b",
                                border_color="#4b4f9d",
                                button_color="black",
                                )

combo_contratos.place(x=30,y=100)

label_datainicio=ctk.CTkLabel(frame5,text="")
label_datafinal=ctk.CTkLabel(frame5,text="")
label_carro=ctk.CTkLabel(frame5,text="")
label_valor=ctk.CTkLabel(frame5,text="")
label_forma_de_pagamento=ctk.CTkLabel(frame5,text="")




frame5.mainloop()