import tkinter as tk

# Cria a janela
root = tk.Tk()
root.title("Listbox")

# Função chamada quando a seleção muda
def selecao_mudou(eventos):
    sel = eventos.widget.curselection()
    itens = [eventos.widget.get(i) for i in sel]

    label.config(text=f"{', '.join(itens)} selecionado(s)!")

# Cria a Listbox
listbox = tk.Listbox(root, selectmode="multiple")

# Adiciona os itens
for item in ["Primeiro", "Segundo", "Terceiro"]:
    listbox.insert(tk.END, item)

# Evento de seleção
listbox.bind("<<ListboxSelect>>", selecao_mudou)

listbox.pack(expand=True)

# Label
label = tk.Label(root, text="Nenhum item selecionado")
label.pack()

# Inicia a aplicação
root.mainloop()