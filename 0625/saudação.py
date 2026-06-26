def saudação (nome="visitante"):
         """função que recebe um nome e retorna uma saudação"""
         return f"olá, {nome}"

nome = input("digite seu nome: ")
print(saudação(nome))