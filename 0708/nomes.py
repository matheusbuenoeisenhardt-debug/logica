nomes = input("digite nomes separados por ', + espaço':").split(", ")
with open("0708/nomes.txt", "w") as f:
        for n in nomes:
            f.write(n + "\n")