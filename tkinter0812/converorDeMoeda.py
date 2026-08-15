import tkinter as tk
from tkinter import ttk

def realizar_conversao():
    try:
        valor = float(entry_valor.get())   #cria a varivel valor de acordo com o que foi inserido em entry_valor
        origem = combo_origem.get()        #cria o valor que sera a base para comparação
        destino = combo_destino.get()      #cria o valor que será comparado

        taxas = {
            "USD": 1.0,
            "BRL": 5.50,
            "EUR": 0.92,
        }

        valor_em_dolar = valor / taxas[origem]                # Converte o valor para dólares
        valor_convertido = valor_em_dolar * taxas[destino]    # Converte de dólares para a moeda de destino

        label_resultado.config(text=f"Resultado: {valor_convertido:.2f} {destino}")
    except ValueError:
        label_resultado.config(text="Erro: Insira um valor numérico válido.")

root = tk.Tk()
root.title("Conversor de Moedas")
root.geometry("300x250")
root.resizable(False, False)

moedas = ["USD", "BRL", "EUR"]


ttk.Label(root, text="Valor:").grid(row=0, column=0, padx=10, pady=10, sticky="E")
entry_valor = ttk.Entry(root)
entry_valor.grid(row=0, column=1, padx=10, pady=10)

ttk.Label(root, text="Moeda de Origem:").grid(row=1, column=0, padx=10, pady=10, sticky="E")
combo_origem = ttk.Combobox(root, values=moedas, state="readonly")
combo_origem.set("BRL")
combo_origem.grid(row=1, column=1, padx=10, pady=10)

ttk.Label(root, text="Moeda de Destino:").grid(row=2, column=0, padx=10, pady=10, sticky="E")
combo_destino = ttk.Combobox(root, values=moedas, state="readonly")
combo_destino.set("USD")
combo_destino.grid(row=2, column=1, padx=10, pady=10)

btn_converter = ttk.Button(root, text="Converter", command=realizar_conversao)
btn_converter.grid(row=3, column=0, columnspan=2, pady=15)


label_resultado = ttk.Label(root, text="")
label_resultado.grid(row=4, column=0, columnspan=2)

root.mainloop()