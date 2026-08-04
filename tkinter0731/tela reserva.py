import tkinter as tk
from tkinter import messagebox

# Definindo a cor bege padrão para todo o projeto
COR_BEGE = "#F5F5DC"

# cria a janela principal
root = tk.Tk()
root.resizable(False, False)
root.config(bg=COR_BEGE)

def encerrar():
    messagebox.showinfo(
        "Encerramento",
        "Você cancelou o login."
    )
    root.destroy()  # Fecha a janela principal
    
def mostrar_estado():
    if checkbox_estado.get():
        txt = "desejo lembrar desse dispositivo"
    else:
        txt = "não desejo lembrar desse dispositivo"
    checkbox.config(text=txt)

def login():
    if

# Título
message = tk.Label(root, text="Faça seu login", font=("Arial", 22, "bold"), bg=COR_BEGE)
message.pack(expand=True)

# Imagem (O bg vai na Label, não no PhotoImage!)
minha_imagem = tk.PhotoImage(file="Profile.png").subsample(3, 3)
label_imagem = tk.Label(root, image=minha_imagem, bg=COR_BEGE, bd=0)
label_imagem.pack(expand=True)

# Usuário
message1 = tk.Label(root, text="Usuário", pady=10, anchor="w", bg=COR_BEGE, bd=0)
message1.pack(expand=False, anchor="w", padx=190)

entry_peso = tk.Entry(root)
entry_peso.pack()

# Senha
message2 = tk.Label(root, text="Senha", pady=10, anchor="w", bg=COR_BEGE, bd=0)
message2.pack(expand=False, anchor="w", padx=190)

entry_senha = tk.Entry(root, show="•")
entry_senha.pack()

# --- FRAME PARA OS BOTÕES ---
# Adicionado bg=COR_BEGE para o container não ficar cinza
frame_botoes = tk.Frame(root, bg=COR_BEGE)
frame_botoes.pack(pady=20)

botao = tk.Button(frame_botoes, text="Entrar", width=12)
botao.pack(side="left", padx=5)

botao2 = tk.Button(frame_botoes, text="Cadastrar", width=12)
botao2.pack(side="left", padx=5)

botao3 = tk.Button(frame_botoes, text="cancelar", width=12, command=encerrar)
botao3.pack(side="left", padx=5)

# --- FRAME INFERIOR ---
checkbox_estado = tk.IntVar()

# Adicionado bg=COR_BEGE
frame_baixo = tk.Frame(root, bg=COR_BEGE)
frame_baixo.pack()

checkbox = tk.Checkbutton(
    frame_baixo,
    text="(deseja lembrar desse dispositivo?)", 
    variable=checkbox_estado, 
    command=mostrar_estado,
    bg=COR_BEGE,
    activebackground=COR_BEGE # Evita que pisque cinza ao clicar
)

checkbox.select()
checkbox.pack(expand=True, padx=10, side="left", anchor="w")

label_esqueceu = tk.Label(frame_baixo, text="esqueceu a senha?", bg=COR_BEGE)
label_esqueceu.pack(expand=True, padx=10, side="left", anchor="w")

root.geometry("500x600+50+50")
root.mainloop()