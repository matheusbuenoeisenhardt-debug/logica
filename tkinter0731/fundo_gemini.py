import tkinter as tk

root = tk.Tk()
root.geometry("400x400")

# Caixa com a cor de fundo (bg) definida
caixa = tk.Frame(root, bg="#3498db", width=250, height=250)
caixa.pack(expand=True)

root.mainloop()