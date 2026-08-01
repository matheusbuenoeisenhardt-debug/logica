#calculadora de imc, requisitos: widgets basicos ou seja usar label entry e button, campos de entrada que são dois entry chamados peso e altura, botão circular que calcula o imc e exibe o resultado em um label, exibir uma mensagem para indicar se está abaixo do peso ou saudavel ou sobrepeso ou obesidade.
import tkinter as tk

# Janela principal
root = tk.Tk()
root.title("Calculadora de IMC")
root.geometry("300x250")

# Função para calcular o IMC
def calcular():
    try:
        peso = float(entry_peso.get()).replace(",", ".")
        altura = float(entry_altura.get())replace(",", ".")

        imc = peso / (altura ** 2)

        if imc < 18.5:
            situacao = "Abaixo do peso"
        elif imc < 25:
            situacao = "Peso normal"
        elif imc < 30:
            situacao = "Sobrepeso"
        else:
            situacao = "Obesidade"

        label_resultado.config(
            text=f"IMC: {imc:.2f}\n{situacao}"
        )

    except ValueError:
        label_resultado.config(
            text="Digite valores válidos!"
        )

# Peso
label_peso = tk.Label(root, text="Peso (kg):")
label_peso.pack()

entry_peso = tk.Entry(root)
entry_peso.pack()

# Altura
label_altura = tk.Label(root, text="Altura (m):")
label_altura.pack()

entry_altura = tk.Entry(root)
entry_altura.pack()

# Botão
botao = tk.Button(root, text="Calcular", command=calcular)
botao.pack(pady=10)

# Resultado
label_resultado = tk.Label(root, text="Informe seu peso e altura.")
label_resultado.pack()

# Executa a janela
root.mainloop()