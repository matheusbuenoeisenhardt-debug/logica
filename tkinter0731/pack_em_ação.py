import tkinter as tk

root = tk.Tk()
root.title("SENAI - Desenvolvimento de Sistemas")
root.geometry("340x100")

# Botão no topo
tk.Button(root, text="Top Button!").pack()

# Labels alinhadas à esquerda e à direita
tk.Label(root, text="Hello, Left!").pack(side="left")
tk.Label(root, text="Hello, Right!").pack(side="right")

# Checkbutton na parte inferior
tk.Checkbutton(root, text="Uma opção na parte inferior!").pack(side=tk.BOTTOM)

root.mainloop()