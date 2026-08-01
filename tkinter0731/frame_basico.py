#o codigo abaixo demonstra como criar e exibir um frame simples usando o metodo pack(), com margens externas definidas por padx e pady:

import tkinter as tk

root = tk.Tk()
root.title("SENAI - Desenvolvimento de Sistemas")
root.config(bg="skyblu")

frame = tk.Frame (root, width=200, height=200)
frame.pack(padx=10, pady=10)

root.mainloop()