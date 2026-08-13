import os
import random
import tkinter as tk
from tkinter import Frame, Label, NW
from PIL import Image, ImageTk           #tem que rodar no terminal o seguinte comando: pip install Pillow
                                         #logo apos use o comando: cd tkinter0812

# --- CORES E CONFIGURAÇÕES ---
cor0 = "#FFFFFF"  # Branco
cor1 = "#000000"  # Preto
cor2 = "#FF9900"  # Laranja (Empate)
cor4 = "#22AA00"  # Verde (Início / Vitória)
cor5 = "#B40000"  # Vermelho (Derrota)
fundo = "#868686"  # Cinza

# Variáveis globais de pontuação
pontos_pessoa = 0
pontos_pc = 0

root = tk.Tk()
root.title("SENAI - Pedra, Papel e Tesoura")
root.geometry("400x500+50+100")
root.resizable(False, False)
root.configure(bg=fundo)

# --- CRIAÇÃO DOS FRAMES ---
frame_cima = Frame(root, width=400, height=150, bg=cor1, relief="flat")
frame_cima.grid(row=0, column=0, sticky=NW)

frame_baixo = Frame(root, width=400, height=350, bg=cor0, relief="flat")
frame_baixo.grid(row=1, column=0, sticky=NW)

# --- CONFIGURANDO AS BARRAS LATERAIS (VERDES NO INÍCIO) ---
app_pessoa_linha = Label(
    frame_cima, text="", width=2, height=9, bg=cor4, relief="flat"
)
app_pessoa_linha.place(x=0, y=0)

app_pc_linha = Label(
    frame_cima, text="", width=2, height=9, bg=cor4, relief="flat"
)
app_pc_linha.place(x=386, y=0)

# --- CONFIGURANDO OS JOGADORES (FRAME CIMA) ---
app_pessoa = Label(
    frame_cima,
    text="Você",
    height=1,
    anchor="center",
    bg=cor1,
    fg=cor0,
    font=("Ivy 10 bold"),
)
app_pessoa.place(x=30, y=70)

app_pessoa_pontos = Label(
    frame_cima,
    text="0",
    height=1,
    anchor="center",
    bg=cor1,
    fg=cor0,
    font=("Ivy 30 bold"),
)
app_pessoa_pontos.place(x=40, y=20)

app_vs = Label(
    frame_cima,
    text=":",
    height=1,
    anchor="center",
    bg=cor1,
    fg=cor0,
    font=("Ivy 30 bold"),
)
app_vs.place(x=190, y=20)

app_pc_pontos = Label(
    frame_cima,
    text="0",
    height=1,
    anchor="center",
    bg=cor1,
    fg=cor0,
    font=("Ivy 30 bold"),
)
app_pc_pontos.place(x=320, y=20)

app_pc = Label(
    frame_cima,
    text="SENAI",
    height=1,
    anchor="center",
    bg=cor1,
    fg=cor0,
    font=("Ivy 10 bold"),
)
app_pc.place(x=310, y=70)


# --- CARREGANDO AS IMAGENS ---
def carregar_imagem(caminho):
  if os.path.exists(caminho):
    img = Image.open(caminho)
    img = img.resize((60, 60), Image.Resampling.LANCZOS)
    return ImageTk.PhotoImage(img)
  else:
    return None


icon_pedra = carregar_imagem("pedra.png")
icon_papel = carregar_imagem("papel.png")
icon_tesoura = carregar_imagem("tesoura.png")

# Labels para exibir a escolha feita no meio da tela
app_l_escolha = Label(frame_baixo, bg=cor0)
app_l_escolha.place(x=80, y=90)

app_pc_escolha = Label(frame_baixo, bg=cor0)
app_pc_escolha.place(x=250, y=90)


# --- LÓGICA DO JOGO ---
def jogar(escolha_usuario):
  global pontos_pessoa, pontos_pc

  opcoes = ["Pedra", "Papel", "Tesoura"]
  escolha_pc = random.choice(opcoes)

  imagens = {"Pedra": icon_pedra, "Papel": icon_papel, "Tesoura": icon_tesoura}

  # Exibe as imagens escolhidas na tela se existirem
  if icon_pedra and icon_papel and icon_tesoura:
    app_l_escolha.config(image=imagens[escolha_usuario])
    app_pc_escolha.config(image=imagens[escolha_pc])

  # Verifica o vencedor e altera as cores laterais
  if escolha_usuario == escolha_pc:
    resultado = "Empate!"
    cor_lateral = cor2  # Laranja
  elif (
      (escolha_usuario == "Pedra" and escolha_pc == "Tesoura")
      or (escolha_usuario == "Papel" and escolha_pc == "Pedra")
      or (escolha_usuario == "Tesoura" and escolha_pc == "Papel")
  ):
    resultado = "Você Ganhou!"
    cor_lateral = cor4  # Verde
    pontos_pessoa += 1
    app_pessoa_pontos.config(text=str(pontos_pessoa))
  else:
    resultado = "SENAI Ganhou!"
    cor_lateral = cor5  # Vermelho
    pontos_pc += 1
    app_pc_pontos.config(text=str(pontos_pc))

  app_pessoa_linha.config(bg=cor_lateral)
  app_pc_linha.config(bg=cor_lateral)
  app_status.config(text=resultado)


# --- ÁREA DO JOGO (FRAME BAIXO) ---
app_texto = Label(
    frame_baixo,
    text="Escolha uma opção abaixo:",
    height=1,
    anchor="center",
    bg=cor0,
    fg=cor1,
    font=("Ivy 12 bold"),
)
app_texto.place(x=90, y=20)

app_status = Label(
    frame_baixo,
    text="",
    height=1,
    anchor="center",
    bg=cor0,
    fg=cor1,
    font=("Ivy 14 bold"),
)
app_status.place(x=130, y=180)

# --- BOTÕES COM IMAGENS ---
btn_pedra = tk.Button(
    frame_baixo,
    image=icon_pedra,
    width=70,
    height=70,
    bg=cor0,
    relief="raised",
    command=lambda: jogar("Pedra"),
)
btn_pedra.image = icon_pedra
btn_pedra.place(x=40, y=240)

btn_papel = tk.Button(
    frame_baixo,
    image=icon_papel,
    width=70,
    height=70,
    bg=cor0,
    relief="raised",
    command=lambda: jogar("Papel"),
)
btn_papel.image = icon_papel
btn_papel.place(x=160, y=240)

btn_tesoura = tk.Button(
    frame_baixo,
    image=icon_tesoura,
    width=70,
    height=70,
    bg=cor0,
    relief="raised",
    command=lambda: jogar("Tesoura"),
)
btn_tesoura.image = icon_tesoura
btn_tesoura.place(x=280, y=240)

root.mainloop()