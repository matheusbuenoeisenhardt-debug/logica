from tkinter import Tk, Canvas    #importa o canvas para o código

janela = Tk()                     #cria a janela

canvas=Canvas(janela, width=400, height=300,bg="yellow")      #cria o canvas

#códigos em sistemas mais complexos

canvas.create_polygon(
         100,50,            #marca as pontas do poligono, x1, y1, x2, y2, x3, y3 e assim por diante
         150,150,
         50,150,
         fill="green",
         outline="gray",
         width=5
)

canvas.pack()         #exibe o canvas
janela.mainloop()