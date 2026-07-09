with open("0708/filmes.txt", "r") as f:
    conteudo = f.read()
    print(conteudo)

print("0 - adicionar filme (opcional)")
print("1 - quantidade total de filmes")
print("2 - informações de um filme pelo titulo")
print("3 - filmes de um diretor especifico")
print("4 - filmes de um genero especifico")
print("5 - media de duração dos filmes")
print("6 - sair")
escolha = input("qual opção deseja escolher: ").strip()

if escolha == 0:
    adicionar_filme()

elif escolha == 1:
    contar_filmes()

elif escolha == 2:
    info_por_titulo()

elif escolha == 3:
    filmes_por_diretor()

elif escolha == 4:
    filmes_por_genero()

elif escolha == 5:
    media_duração()

elif escolha == 6:
    print("encerrando sistema")
    break 

else:
    print("opção invalida, digite novamente.")