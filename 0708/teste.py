# Exemplos de leitura:

# Usando o método read() -> Lê o arquivo inteiro de uma vez
with open("0708/exemplo.txt", "r") as f:
    conteudo = f.read()
    print(conteudo)

print("------------------------------")

# Usando o método readline() -> Lê uma linha por vez
with open("0708/exemplo.txt", "r") as f:
    linha1 = f.readline()
    linha2 = f.readline()
    print(linha1, end="")
    print(linha2, end="")

print("------------------------------")

# Iterando direto no arquivo -> O jeito mais eficiente para arquivos grandes
with open("0708/exemplo.txt", "r") as f:
    for linha in f:
        print(linha, end="")

print("----------------------------")

with open("0708/exemplo.txt") as f:
    print(f.read())

    print("----------------------------")