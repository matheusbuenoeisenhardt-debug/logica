from tkinter import Tk, Canvas    #importa o canvas para o código

janela = Tk()                     #cria a janela

canvas=Canvas(janela, width=400, height=300,bg="yellow")      #cria o canvas

#códigos em sistemas mais complexos

canvas.create_rectangle(             #quadrado azul com borda vermelha adicionado nas cordenadas do canvas
         50, 50, 150, 250,           #x1, y1, x2, y2  #igual o comando /fill do minecraft
         fill="blue",
         outline="red"
)

canvas.create_oval(             #circulo verde com borda rosa adicionado nas cordenadas do canvas
         150, 50, 300, 250,          #x1, y1, x2, y2  #igual o comando /fill do minecraft mas redondo
         fill="green",
         outline="pink"
)

canvas.create_line(             #cria uma linha preda que vai da ponta x1, y1, ate a ponta x2, y2
         10, 10, 200, 200,          
         fill="black",
         width=4
)

canvas.create_line(             #cria uma linha preda que vai da ponta x1, y1, ate a ponta x2, y2
         10, 10, 10, 200,          
         fill="black",
         width=4
)

canvas.pack()         #exibe o canvas
janela.mainloop()