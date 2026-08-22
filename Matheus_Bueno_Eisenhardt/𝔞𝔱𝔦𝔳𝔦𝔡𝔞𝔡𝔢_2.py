numero_inicial = int(input("digite o numero inicial: "))
numero_final = int(input("digite o numero inicial: "))

print(f"os numeros pares entre {numero_inicial} e {numero_final} são:")
for i in range(numero_inicial, numero_final + 1):
    if i % 2 == 0:
        print(i)
    