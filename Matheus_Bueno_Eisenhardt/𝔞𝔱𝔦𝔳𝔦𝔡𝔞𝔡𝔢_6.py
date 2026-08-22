valores = []

while True:
    numero = int(input("digite o valor que pretende adicionar a lista (digite 0 para encerrar)"))
    if numero == 0:
        break
    valores.append(numero)

if valores:
    meio = len(valores) // 2
    print(f"\nlista completa = {valores}")
    print(f"valor central = {valores[meio]}")

else:
    print("nenhum valor foi inserido")