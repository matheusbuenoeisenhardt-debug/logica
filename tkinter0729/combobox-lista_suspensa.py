import tkinter as tk
from tkinter import ttk  # Importação que faltava

root = tk.Tk()
root.title("Exemplo Combobox")

def selecao_mudou(evento):
    label.config(text=f"{evento.widget.get()} selecionado!")

# 'Combobox' com C maiúsculo
combobox = ttk.Combobox(root, values=["primeiro", "segundo", "terceiro", "quarto"])
combobox.set("abra!!!")
combobox.bind("<<ComboboxSelected>>", selecao_mudou)
combobox.pack()

# 'Label' com L maiúsculo
label = tk.Label(root, text="primeiro selecionado!")
label.pack()

# Necessário para manter a janela rodando
root.mainloop()