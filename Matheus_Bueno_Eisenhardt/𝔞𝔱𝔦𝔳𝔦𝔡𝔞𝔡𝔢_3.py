senha = input("digite uma senha: ")

tamanho = len(senha) >= 8
maiusculo = any(c.isupper() for c in senha)
minusculo = any(c.islower() for c in senha)
numero = any(c.isdigit() for c in senha)

if tamanho and maiusculo and minusculo and numero:
    print("senha forte!")

else:
    print("senha fraca.")