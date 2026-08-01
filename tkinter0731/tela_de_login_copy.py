import tkinter as tk

#cria a janela principal
root = tk.Tk()

message = tk.Label(root, text="Faça seu login", anchor="w", font=("bold", 28, "bold"))
message.pack(expand=True)

minha_imagem = tk.PhotoImage(file="Profile.png").subsample(3,3)

label = tk.Label(root, image=minha_imagem)
label.pack(expand=True)

#cria um rótulo (label) com o texto "Hello World!"
message1 = tk.Label(root, text="Usuário", pady=10, anchor="w")
message1.pack(expand=False, anchor="w", padx=190)  

entry_peso = tk.Entry(root)
entry_peso.pack()

message2 = tk.Label(root, text="Senha", pady=10, anchor="w")
message2.pack(expand=False, anchor="w", padx=190)

entry_senha = tk.Entry(root, show="*")
entry_senha.pack()

botao = tk.Button(root, text="entrar", width=20)
botao.pack(pady=20, anchor="w", padx=90)

botao2 = tk.Button(root, text="entrar", width=20)
botao2.pack(pady=20, anchor="e", padx=90)

#inicia o loop principal da interface gráfica
root.geometry ("500x600+50+50")

root.mainloop()
