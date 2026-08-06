import tkinter as tk

root = tk.Tk()
root.title("SENAI - desenvolvimento de sistemas")
# Ajustado o tamanho da janela para caber os botões grandes
root.geometry("750x550")

for linha in range(3):
    for coluna in range(3):
        tk.Button(
            root,
            text=f"cell({linha}, {coluna})",
            width=20,  # Corrigido de wigth para width
            height=5
        ).grid(row=linha, column=coluna, padx=2, pady=2)

tk.Button(
    root,
    text="Span 2 columns",
    height=5
).grid(row=3, column=0, columnspan=2, sticky="ew", padx=2, pady=2)

tk.Button(
    root,
    text="Span 2 rows",
    width=20
).grid(row=3, column=2, rowspan=2, sticky="ns", padx=2, pady=2)  # Alterado para rowspan e ajustado a posição

root.mainloop()  # Corrigido: adicionado os parênteses ()