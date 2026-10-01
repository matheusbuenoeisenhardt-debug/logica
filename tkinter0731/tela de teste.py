import tkinter as tk
from tkinter import messagebox

# Definindo a cor bege padrão para todo o projeto
COR_BEGE = "#F5F5DC"

# cria a janela principal
root = tk.Tk()
root.resizable(False, False)
root.config(bg=COR_BEGE)

def registrar():
    usuario = entry_usuario.get()
    senha = entry_senha.get()

    if not usuario or not senha:
        messagebox.showwarning("Aviso", "Preencha todos os campos!")
        return

    # Tenta ler o arquivo. Se não existir, ignora o erro e continua.
    conteudo = ""
    try:
        with open("registros.txt", "r", encoding="utf-8") as f:
            conteudo = f.read()
    except FileNotFoundError:
        pass 

    if f"Usuario: {usuario}" in conteudo:
        messagebox.showerror("Erro", "Usuário já cadastrado.")
        entry_usuario.delete(0, tk.END)
        entry_senha.delete(0, tk.END)
        return
    
    with open("registros.txt", "a", encoding="utf-8") as f:
        f.write(f"Usuario: {usuario}\n")
        f.write(f"Senha: {senha}\n")
        
    messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
    entry_usuario.delete(0, tk.END)
    entry_senha.delete(0, tk.END)

def encerrar():
    messagebox.showinfo("Encerramento", "Você cancelou o login.")
    root.destroy()
    
def mostrar_estado():
    if checkbox_estado.get():
        txt = "Desejo lembrar desse dispositivo"
    else:
        txt = "Não desejo lembrar desse dispositivo"
    checkbox.config(text=txt)

def login():
    usuario_buscado = entry_usuario.get()
    senha_inserida = entry_senha.get()

    try:
        with open("registros.txt", "r", encoding="utf-8") as f:
            linhas = f.readlines()
            
        for i in range(len(linhas)):
            # Trocamos o 'in' por '==' para exigir que o nome seja EXATAMENTE igual
            if linhas[i].strip() == f"Usuario: {usuario_buscado}":
                
                # Trocamos o 'in' por '==' para exigir que a senha seja EXATAMENTE igual
                if i + 1 < len(linhas) and linhas[i+1].strip() == f"Senha: {senha_inserida}":
                    messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
                    
                    # Esconde a tela de login atual
                    root.withdraw()
                    # Chama a sua nova tela aqui, ex: abrir_tela_principal()
                    
                    return 
                
                else:
                    messagebox.showerror("Erro", "Senha incorreta.")
                    return 
                    
        messagebox.showerror("Erro", "Usuário não encontrado.")

    except FileNotFoundError:
        messagebox.showerror("Erro", "Nenhum usuário cadastrado ainda.")

# Título
message = tk.Label(root, text="Faça seu login", font=("Arial", 22, "bold"), bg=COR_BEGE)
message.pack(expand=True)

# Imagem (Use um try/except para evitar crash caso a imagem não exista)
try:
    minha_imagem = tk.PhotoImage(file="Profile.png").subsample(3, 3)
    label_imagem = tk.Label(root, image=minha_imagem, bg=COR_BEGE, bd=0)
    label_imagem.pack(expand=True)
except tk.TclError:
    print("Aviso: Imagem Profile.png não encontrada.")

# Usuário
message1 = tk.Label(root, text="Usuário", pady=10, anchor="w", bg=COR_BEGE, bd=0)
message1.pack(expand=False, anchor="w", padx=190)

entry_usuario = tk.Entry(root)
entry_usuario.pack()

# Senha
message2 = tk.Label(root, text="Senha", pady=10, anchor="w", bg=COR_BEGE, bd=0)
message2.pack(expand=False, anchor="w", padx=190)

entry_senha = tk.Entry(root, show="•")
entry_senha.pack()

# --- FRAME PARA OS BOTÕES ---
frame_botoes = tk.Frame(root, bg=COR_BEGE)
frame_botoes.pack(pady=20)

# O botão Entrar agora tem command=login
botao = tk.Button(frame_botoes, text="Entrar", width=12, command=login)
botao.pack(side="left", padx=5)

botao2 = tk.Button(frame_botoes, text="Cadastrar", width=12, command=registrar)
botao2.pack(side="left", padx=5)

botao3 = tk.Button(frame_botoes, text="Cancelar", width=12, command=encerrar)
botao3.pack(side="left", padx=5)

# --- FRAME INFERIOR ---
checkbox_estado = tk.IntVar()

frame_baixo = tk.Frame(root, bg=COR_BEGE)
frame_baixo.pack()

checkbox = tk.Checkbutton(
    frame_baixo,
    text="(deseja lembrar desse dispositivo?)", 
    variable=checkbox_estado, 
    command=mostrar_estado,
    bg=COR_BEGE,
    activebackground=COR_BEGE
)

checkbox.select()
checkbox.pack(expand=True, padx=10, side="left", anchor="w")

label_esqueceu = tk.Label(frame_baixo, text="Esqueceu a senha?", bg=COR_BEGE)
label_esqueceu.pack(expand=True, padx=10, side="left", anchor="w")

root.geometry("500x600+50+50")
root.mainloop()