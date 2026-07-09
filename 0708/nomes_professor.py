print('digite nomes (precione enter em branco para encerrar o programa)')
nomes = []
while True:
      nome = input('digite um nome: ')
      if nome == "":
        break
      nomes.append(nome)
with open("0708/nomes.txt", "w", encoding="utf-8") as f:
        for n in nomes:
            f.write(n + "\n")