import tkinter as tk
root = tk.Tk()
root.title("SENAI - Desenvolvimento de Sistemas")

#ler o titulo da janela
title = root.title()

#Cria o rótulo (label) com o título de janela 
message = tk.Label(root, text="litle")

#posiciona o rótilo da janela
message.pack()

#define o tamanho da janela (largura x altura + posiciona x + posição y)
root.geometry ("400x200+50+250")

root.mainloop() #Inicia o sistema de loop principal da interface gráfica, que mantém a janela aberta e aguarda eventos do usuário, como cliques de botão ou entrada de teclado.