from tkinter import Tk, Canvas    #importa o canvas para o código

janela = Tk()                     #cria a janela

canvas=Canvas(janela, width=400, height=300,bg="yellow")      #cria o canvas

#códigos em sistemas mais complexos

canvas.pack()         #exibe o canvas
janela.mainloop()