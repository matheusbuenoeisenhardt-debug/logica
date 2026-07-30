import tkinter as tk
minha_imagem = tk.PhotoImage(file="minha-imagem.jfif")

label = tk.label(root, image=minha_imagem)
label.pack(expand=True)