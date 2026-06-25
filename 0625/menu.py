l = int(input("digite o numero de linhas: "))
c = int(input("digite o numero de colunas: "))

print("+" + ("-" * l) + "+")

for x in range(c):
         print("|" + (" " * l) + "|")

print("+" + ("-" * l) + "+")

print("\rretangulo pronto!")