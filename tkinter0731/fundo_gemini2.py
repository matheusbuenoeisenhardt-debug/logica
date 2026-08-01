import tkinter as tk

root = tk.Tk()
root.geometry("400x300")

# Primeira caixa (Esquerda)
caixa1 = tk.Frame(root, bg="#8D8D04", width=150, height=200)
caixa1.pack(side="top", expand=True)

# Segunda caixa (Direita)
caixa2 = tk.Frame(root, bg="#C0C07D", width=150, height=200)
caixa2.pack(side="top", expand=True)

root.mainloop()