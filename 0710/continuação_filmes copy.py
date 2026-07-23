with open("0708/filmes.txt", "r") as f:
    conteudo = f.read()
    print(conteudo)

def menu():
    print(conteudo)
    print("0 - adicionar filme (opcional)")
    print("1 - quantidade total de filmes")
    print("2 - informações de um filme pelo titulo")
    print("3 - filmes de um diretor especifico")
    print("4 - filmes de um genero especifico")
    print("5 - media de duração dos filmes")
    print("6 - sair")

def adicionar_filme():
         titulo = input("Digite o titulo do filme: ")
         diretor = input("insira qual o diretor do filme: ")
         genero = input("insira o genero ao qual o filme pertence: ")
         duracao = input("insira a duracao do filme em minutos: ")
         with open("0708/filmes.txt", "a") as f:
             f.write(f'\ntitulo = {titulo}\n')
             f.write(f'diretor = {diretor}\n')
             f.write(f'genero = {genero}\n')
             f.write(f'duracao = {duracao}\n')

def contar_filmes():
         contador = 0
         try:
            with open("0708/filmes.txt", "r" ) as f:
                for linha in f:
                    if linha.strip().startwith("Titulo"): #linha.strip() remove espaços em branco no início e no final da linha, e startwith() verifica se a linha começa com a palavra "Titulo"
                        contador += 1
            print(f"quantidade de filmes cadastrados: {contador}")
         except FileNotFoundError:
                  print("arquivo não encontrado.")

         print(f"quantidade de filmes: {contador}")

def info_por_titulo():
            titulo_buscaado = input("Digite o titulo do filme: ").strip().lower() #pede o titulo do filme e transforma em minusculo para facilitar a busca, alem de retirar os espaços em branco no inicio e no final da string
            encontrado = False
            try:
                with open("0708/filmes.txt", "r") as f: #abre o arquivo e renomeia ele para f, facilitando a leitura do arquivo
                        for linha in f:
                            if linha.strip().startwith ("Titulo:"):
                                    titulo = linha.strip().split(":", 1)[1].strip()
                                    if titulo.lower() == titulo_buscaado:
                                    print(f"titulo: {titulo}")
                                    try:
                                        ano = next(f).strip()
                                        diretor = next(f).strip()
                                        genero = next(f).strip()
                                        duracao = next(f).strip()
                                    except FileNotFoundError:
                                        print("arquivo não encontrado.")
                                        return
                                    print(ano)
                                    print(diretor)
                                    print(genero)
                                    print(duracao)
                                    encontrado = True
                                    break

           
def filmes_por_diretor():
         print(" ")

def filmes_por_genero():
         print(" ")

def media_duração():
         print(" ")

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