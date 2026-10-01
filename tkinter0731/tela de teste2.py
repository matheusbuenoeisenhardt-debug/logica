import tkinter as tk
from tkinter import messagebox

# Definindo a cor bege padrão para todo o projeto
COR_BEGE = "#F5F5DC"

# --- FUNÇÃO DA NOVA TELA ---
def abrir_tela_principal(nome_usuario):
    # Cria a nova janela usando Toplevel (janela secundária)
    tela_principal = tk.Toplevel()
    tela_principal.title("Área Logada")
    tela_principal.geometry("400x300+100+100")
    tela_principal.config(bg="#ADD8E6") # Azul claro para diferenciar

    # Dá as boas vindas com o nome do usuário que logou
    mensagem = tk.Label(tela_principal, text=f"Bem-vindo(a), {nome_usuario}!", font=("Arial", 18, "bold"), bg="#ADD8E6")
    mensagem.pack(pady=50)

    # Botão para encerrar de vez o programa (destrói o root que estava escondido)
    botao_sair = tk.Button(tela_principal, text="Sair do Programa", command=root.destroy, width=15)
    botao_sair.pack()

# --- FUNÇÕES DE LÓGICA DO LOGIN ---
def registrar():
    usuario = entry_usuario.get()
    senha = entry_senha.get()

    if not usuario or not senha:
        messagebox.showwarning("Aviso", "Preencha todos os campos!")
        return

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
            # Usando == para exigir a palavra exata (evita o erro do "gay123")
            if linhas[i].strip() == f"Usuario: {usuario_buscado}":
                if i + 1 < len(linhas) and linhas[i+1].strip() == f"Senha: {senha_inserida}":
                    messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
                    
                    # 1. Esconde a tela de login principal
                    root.withdraw()
                    
                    # 2. Chama a nova tela passando o nome do usuário
                    abrir_tela_principal(usuario_buscado)
                    return
                else:
                    messagebox.showerror("Erro", "Senha incorreta.")
                    return
                    
        messagebox.showerror("Erro", "Usuário não encontrado.")

    except FileNotFoundError:
        messagebox.showerror("Erro", "Nenhum usuário cadastrado ainda.")


# --- INTERFACE GRÁFICA (TELA DE LOGIN) ---
root = tk.Tk()
root.resizable(False, False)
root.config(bg=COR_BEGE)
root.title("Sistema de Login")

# Título
message = tk.Label(root, text="Faça seu login", font=("Arial", 22, "bold"), bg=COR_BEGE)
message.pack(expand=True, pady=10)

# Imagem
try:
    minha_imagem = tk.PhotoImage(file="Profile.png").subsample(3, 3)
    label_imagem = tk.Label(root, image=minha_imagem, bg=COR_BEGE, bd=0)
    label_imagem.pack(expand=True)
except tk.TclError:
    print("Aviso: Imagem Profile.png não encontrada.")

# Usuário
message1 = tk.Label(root, text="Usuário", pady=5, anchor="w", bg=COR_BEGE, bd=0)
message1.pack(expand=False, anchor="w", padx=150)

entry_usuario = tk.Entry(root)
entry_usuario.pack(pady=5)

# Senha
message2 = tk.Label(root, text="Senha", pady=5, anchor="w", bg=COR_BEGE, bd=0)
message2.pack(expand=False, anchor="w", padx=150)

entry_senha = tk.Entry(root, show="•")
entry_senha.pack(pady=5)

# --- FRAME PARA OS BOTÕES ---
frame_botoes = tk.Frame(root, bg=COR_BEGE)
frame_botoes.pack(pady=20)

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