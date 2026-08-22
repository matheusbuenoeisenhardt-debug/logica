with open ("Matheus_Bueno_Eisenhardt/usuario.txt", "w", encoding="utf-8") as r:
    for i in range (3):
        nome = input(f"digite o {i + 1}° nome: ")
        r.write(nome + "\n")

print("nomes salvos com sucesso em usuario.txt")