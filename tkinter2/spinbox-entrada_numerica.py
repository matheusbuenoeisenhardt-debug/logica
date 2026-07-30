import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Inicializa a janela principal
root = tk.Tk()
root.title("Exemplo Spinbox")
root.geometry("300x200")

# StringVar é uma variável que armazena uma string
# e é usada para atualizar widget dinamicamente
spinbox_var = tk.StringVar(value="0")

spinbox = tk.Spinbox(
    root,
    from_=-10,
    to=10,
    # increment=5,
    textvariable=spinbox_var
)

spinbox.pack(expand=True)

label = tk.Label(root, textvariable=spinbox_var)
label.pack()

# Executa a aplicação
root.mainloop()