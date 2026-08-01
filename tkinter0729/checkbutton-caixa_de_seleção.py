import tkinter as tk
from tkinter import messagebox

# 1. Criação da janela principal
root = tk.Tk()
root.title("Exemplo de Checkbutton")
root.geometry("3000x150")

# 2. Criação da variável do Tkinter (DEPOIS de criar o root)
checkbox_estado = tk.IntVar()

# 3. Função de callback
def mostrar_estado():
    if checkbox_estado.get():
        txt = "Checked"
    else:
        txt = "Unchecked"
    checkbox.config(text=f"Check me! ({txt})")

# 4. Criação do Checkbutton (Com 'C' maiúsculo)
checkbox = tk.Checkbutton(
    root,
    text="Check me! (Checked)", 
    variable=checkbox_estado, 
    command=mostrar_estado
)

checkbox = tk.Checkbutton(
    root,
    text="Check me! (Checked)", 
    variable=checkbox_estado, 
    command=mostrar_estado
)

# Configuração inicial
checkbox.deselect()        #como o botão vai aparecer, select vai aparecer selecionado e deselect vai aparecer deselecionado
checkbox.pack(expand=True) #centraliza o componente no meio da tela

# 5. Loop principal para manter a janela aberta
root.mainloop()