import tkinter as tk

#cria a janela principal
root = tk.Tk()

#cria um rótulo (label) com o texto "Hello World!"
message = tk.Label(root, text="Hello World!")

#posiciona o rótulo na janela
message .pack()

#inicia o loop principal da interface gráfica
root.geometry ("400x200+50+50")

root.mainloop()