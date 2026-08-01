import tkinter as tk

#cria a janela principal
root = tk.Tk()


minha_imagem = tk.PhotoImage(file="logo.png").subsample(3,3)

label = tk.Label(root, image=minha_imagem)
label.pack(expand=True)



#inicia o loop principal da interface gráfica
root.geometry ("700x500")

root.mainloop()