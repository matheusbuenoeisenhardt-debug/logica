import tkinter as tk
from tkinter import messagebox
from tkinter import Frame

cor0 = "#FFFFFF"
cor1 = "#000000"
cor2 = "#FF9900"
cor3 = "#ECF000"
cor4 = "#22AA00"
cor5 = "#B40000"
fundo = "#868686"
root = tk.Tk()
root.title("SENAI - pedra, papel e tesoura")
root.geometry("400x500+50+100")
root.resizable(False, False)
root.configure(bg=fundo)

frame_cima = Frame(janela,widht=260, height=100, bg=cor1, relief="raised")
frame_cima.grid(row=0, column=0, sticky=NW)

frame_baixo = Frame(janela, width=260,height=300, bg=cor0, relief="flat")
frame_baixo.grid(row=1, column=0, sticky=NW)

#configurando os jogadores
#jogador pessoa
app_pessoa = Label(frame_cima, text="jogador", height=1, anchor="center", bg=cor1, fg=cor0, font=("Ivy 10 bold"))
app_pessoa.place(x=10, y=70)

#barra marcou pontos
app_pessoa_linha = Label(frame_cima, text="", height=1, anchor="center", bg=cor4, fg=cor0, font=("Ivy 10 bold"))
app_pessoa_linha.place(x=50, y=20)

#pontuação
app_pessoa_pontos = Label(frame_cima, text="0", height=1, anchor="center", bg=cor1, fg=cor0, font=("Ivy 30 bold"))
app_pessoa_pontos.place(x=50, y=20)

#separação da pontuação
app_vs = Label(frame_cima, text=":", height=1, anchor="center", bg=cor1, fg=cor0, font=("Ivy 30 bold"))
app_vs.place(x=125, y=20)


root.mainloop()