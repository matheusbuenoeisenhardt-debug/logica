with open("0708/filmes.txt", "r") as f:
    conteudo = f.read()
    print(conteudo)

def menu():
    print("0 - adicionar filme (opcional)")
    print("1 - quantidade total de filmes")
    print("2 - informações de um filme pelo titulo")
    print("3 - filmes de um diretor especifico")
    print("4 - filmes de um genero especifico")
    print("5 - media de duração dos filmes")
    print("6 - sair")

def adicionar_filme():
    titulo = input("Digite o titulo do filme: ")
    diretor = input("Digite o nome do diretor: ")
    genero = input("Digite o genero do filme: ")
    duracao = input("Digite a duracao do filme (em minutos): ")

    with open("0708/filmes.txt", "a") as f:
        f.write(f"{titulo},{diretor},{genero},{duracao}\n")
    print(f"Filme '{titulo}' adicionado com sucesso!\n")

def contar_filmes():
         contador = 0
         try:
         with open("0708/filmes.txt", encoding="utf-8", "r" ) as f:
                  for linha in f:
                       if linha.strip().startwith("Titulo"): #linha.strip() remove espaços em branco no início e no final da linha, e startwith() verifica se a linha começa com a palavra "Titulo"
                            contador += 1
         print(f"quantidade de filmes cadastrados: {contador}")
         except FileNotFoundError:
                  print("arquivo não encontrado.")

         print(f"quantidade de filmes: {contador}")

def info_por_titulo():
    titulo = input("Digite o titulo do filme: ")
    with open("0708/filmes.txt", "r") as f:
        conteudo = f.readlines()
        for linha in conteudo:
            filme_info = linha.strip().split(",")
            if filme_info[0].lower() == titulo.lower():
                print(f"Titulo: {filme_info[0]}")
                print(f"Diretor: {filme_info[1]}")
                print(f"Genero: {filme_info[2]}")
                print(f"Duracao: {filme_info[3]} minutos\n")
                return
    print("Filme não encontrado.\n")

def filmes_por_diretor():
    diretor = input("Digite o nome do diretor: ")
    with open("0708/filmes.txt", "r") as f:
        conteudo = f.readlines()
        filmes_encontrados = [linha.strip() for linha in conteudo if linha.strip().split(",")[1].lower() == diretor.lower()]
        if filmes_encontrados:
            print(f"Filmes do diretor {diretor}:")
            for filme in filmes_encontrados:
                print(f"- {filme.split(',')[0]}")
            print()
        else:
            print("Nenhum filme encontrado para este diretor.\n")

def filmes_por_genero():
    genero = input("Digite o genero do filme: ")
    with open("0708/filmes.txt", "r") as f:
        conteudo = f.readlines()
        filmes_encontrados = [linha.strip() for linha in conteudo if linha.strip().split(",")[2].lower() == genero.lower()]
        if filmes_encontrados:
            print(f"Filmes do genero {genero}:")
            for filme in filmes_encontrados:
                print(f"- {filme.split(',')[0]}")
            print()
        else:
            print("Nenhum filme encontrado para este genero.\n")

def media_duração():
    with open("0708/filmes.txt", "r") as f:
        conteudo = f.readlines()
        if not conteudo:
            print("Nenhum filme encontrado.\n")
            return
        total_duração = sum(int(linha.strip().split(",")[3]) for linha in conteudo)
        media = total_duração / len(conteudo)
    print(f"Media de duração dos filmes: {media:.2f} minutos\n")

while True:
         
    menu()

    escolha = input("qual opção deseja escolher: ").strip()

    if escolha == "0":
        adicionar_filme()

    elif escolha == "1":
        contar_filmes()

    elif escolha == "2":
        info_por_titulo()

    elif escolha == "3":
        filmes_por_diretor()

    elif escolha == "4":
        filmes_por_genero()

    elif escolha == "5":
        media_duração()

    elif escolha == "6":
        print("encerrando sistema")
        break 

    else:
        print("opção invalida, digite novamente.")