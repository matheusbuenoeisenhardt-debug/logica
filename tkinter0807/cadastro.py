import tkinter as tk
from tkinter import ttk 
from tkinter import messagebox

def enviar_formulario(root, campos):
    # Coleta os valores dos widgets para exibir na mensagem
    nome = campos[0][1].get()
    genero = campos[1][1].get()
    olhos = campos[2][1].get()
    altura = campos[3][1].get()
    peso = campos[4][1].get()
    
    messagebox.showinfo("Sucesso", f"Seu nome é: {nome}\nSeu gênero é: {genero}\nSua cor dos olhos é: {olhos}\nSua altura é: {altura}\nSeu peso é: {peso}")
    root.destroy()

def iniciar_app():
    root = tk.Tk()
    root.title("Formulário de Cadastro")
    root.geometry("700x260")
    root.resizable(False, False)

    root.columnconfigure(1, weight=1)
    root.columnconfigure(2, weight=1)

    try:
        photo = tk.PhotoImage(file="tkinter0731/Profile.png").subsample(3, 3)
        img_label = tk.Label(root, image=photo)
        img_label.image = photo  # Mantém a referência da imagem para não ser apagada pelo garbage collector
        img_label.grid(row=0, column=0, rowspan=6, padx=10, pady=10)
    except:
        img_label = tk.Label(root, text="[Imagem\nPerfil]", bg="gray", width=15, height=8)
        img_label.grid(row=0, column=0, rowspan=6, padx=10, pady=10)

    # Definindo os campos com a criação correta dos widgets vinculados à janela 'root'
    campos = [
        ("Nome:", tk.Entry(root), "entrada"),
        ("Gênero:", ttk.Combobox(root, state="readonly", values=["Masculino", "Feminino"]), "combo"),
        ("Cor dos Olhos:", tk.Entry(root), "entrada"),
        ("Altura (cm):", tk.Entry(root), "entrada"),
        ("Peso (kg):", tk.Entry(root), "entrada")
    ]

    for i, (texto, widget, tipo) in enumerate(campos):
        lbl = tk.Label(root, text=texto)
        lbl.grid(row=i, column=1, sticky="w", padx=5, pady=5)

        widget.grid(row=i, column=2, sticky="ew", padx=5, pady=5)

        if tipo == "combo":
            widget.config(width=15)

    btn_enviar = tk.Button(root, text="Enviar", command=lambda: enviar_formulario(root, campos))
    btn_enviar.grid(row=5, column=1, columnspan=2, sticky="e", padx=5, pady=10)

    root.mainloop()

if __name__ == "__main__":
    iniciar_app()