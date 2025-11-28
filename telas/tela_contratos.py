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


frame5.mainloop()