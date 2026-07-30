import tkinter as tk

root = tk.Tk()
root.title("Exemplo de Listbox")
root.geometry("300x150")  # Corrigido o tamanho da janela

def selecao_mudou(evento):
    sel = evento.widget.curselection()
    if sel:
        idx = sel[0]  # Corrigido: uso de colchetes [] em vez de chaves {}
        label.config(text=f"{evento.widget.get(idx)} selecionado!")

# Corrigido: tk.Listbox com L maiúsculo
listbox = tk.Listbox(root)

for item in ["primeiro", "segundo", "terceiro"]:
    listbox.insert(tk.END, item)  # Corrigido: tk.END em maiúsculas

# Corrigido: nome da função com sublinhado (selecao_mudou)
listbox.bind("<<ListboxSelected>>", selecao_mudou)
listbox.pack(expand=True)

# Corrigido: tk.Label com L maiúsculo
label = tk.Label(root, text="primeiro selecionado!")
label.pack()  # Corrigido: adicionado os parênteses ()

# Adicionado: loop principal para rodar a interface
root.mainloop()