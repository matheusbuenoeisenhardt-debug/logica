with open("0708/filmes.txt", "r") as f:
    conteudo = f.read()

def filmes():
    print(conteudo)

def menu():
    print("\n--- MENU DE FILMES ---")
    filmes()
    print("0 - Adicionar filme")
    print("1 - Quantidade total de filmes")
    print("2 - Informações de um filme pelo título")
    print("3 - Filmes de um diretor específico")
    print("4 - Filmes de um gênero específico")
    print("5 - Média de duração dos filmes")
    print("6 - Sair")


def adicionar_filme():
    titulo = input("Digite o título do filme: ")
    ano = input("Insira o ano do filme: ")
    diretor = input("Insira o diretor do filme: ")
    genero = input("Insira o gênero do filme: ")
    duracao = input("Insira a duração em minutos (ex: 120): ")
    
    with open("0708/filmes.txt", "a", encoding="utf-8") as f:
        f.write(f"\n\nTitulo: {titulo}\n")
        f.write(f"Ano: {ano}\n")
        f.write(f"Diretor: {diretor}\n")
        f.write(f"Genero: {genero}\n")
        f.write(f"Duracao: {duracao} minutos\n")
    print("Filme cadastrado com sucesso!")


def contar_filmes():
    contador = 0
    try:
        with open("0708/filmes.txt", "r", encoding="utf-8") as f:
            for linha in f:
                if "Titulo:" in linha:
                    contador += 1
        print(f"Quantidade de filmes cadastrados: {contador}")
    except FileNotFoundError:
        print("Arquivo '0708/filmes.txt' não encontrado.")


def info_por_titulo():
    titulo_buscado = input("Digite o título do filme: ").strip().lower()
    encontrado = False
    
    try:
        with open("0708/filmes.txt", "r", encoding="utf-8") as f:
            for linha in f:
                if "Titulo:" in linha:
                    # Extrai o título ignorando o que estiver antes de "Titulo:"
                    titulo = linha.split("Titulo:", 1)[1].strip()
                    
                    if titulo.lower() == titulo_buscado:
                        print(f"\nTítulo: {titulo}")
                        try:
                            # Lê as próximas 4 linhas (Ano, Diretor, Gênero, Duração)
                            print(next(f).strip())
                            print(next(f).strip())
                            print(next(f).strip())
                            print(next(f).strip())
                        except StopIteration:
                            print("(Informações incompletas no arquivo)")
                        
                        encontrado = True
                        break
                        
            if not encontrado:
                print("Filme não encontrado.")
    except FileNotFoundError:
        print("Arquivo '0708/filmes.txt' não encontrado.")


def filmes_por_diretor():
    contador = 0
    try:
        with open("0708/filmes.txt", "r", encoding="utf-8") as f:
            diretor_buscado = input("Digite o nome do diretor: ").strip().lower()
            ultimo_titulo = ""
            
            for linha in f:
                s = linha.strip()
                if "Titulo:" in s:
                    ultimo_titulo = s.split("Titulo:", 1)[1].strip()
                elif s.lower().startswith("diretor:"):
                    diretor = s.split(":", 1)[1].strip()
                    if diretor_buscado in diretor.lower():
                        contador += 1
                        print(f"- {ultimo_titulo}")
                        
        print(f"Total de filmes encontrados do diretor '{diretor_buscado}': {contador}")
    except FileNotFoundError:
        print("Arquivo '0708/filmes.txt' não encontrado.")


def filmes_por_genero():
    contador = 0
    try:
        with open("0708/filmes.txt", "r", encoding="utf-8") as f:
            genero_buscado = input("Digite o gênero desejado: ").strip().lower()
            ultimo_titulo = ""
            
            for linha in f:
                s = linha.strip()
                if "Titulo:" in s:
                    ultimo_titulo = s.split("Titulo:", 1)[1].strip()
                elif s.lower().startswith("genero:"):
                    genero = s.split(":", 1)[1].strip()
                    # Usa 'in' para funcionar caso o filme tenha múltiplos gêneros (ex: Crime, Drama)
                    if genero_buscado in genero.lower():
                        contador += 1
                        print(f"- {ultimo_titulo}")
                        
        print(f"Total de filmes no gênero '{genero_buscado}': {contador}")
    except FileNotFoundError:
        print("Arquivo '0708/filmes.txt' não encontrado.")


def media_duracao():
    soma = 0
    cont = 0
    try:
        with open("0708/filmes.txt", "r", encoding="utf-8") as f:
            for linha in f:
                s = linha.strip()
                if s.lower().startswith("duracao:"):
                    try:
                        # Pega o valor logo após 'Duracao:' e extrai apenas o número
                        valor = s.split(":", 1)[1].strip().split()[0]
                        minutos = int(valor)
                        soma += minutos
                        cont += 1
                    except (ValueError, IndexError):
                        continue
    except FileNotFoundError:
        print("Arquivo '0708/filmes.txt' não encontrado.")
        return

    if cont == 0:
        print("Nenhuma duração válida encontrada.")
    else:
        media = soma / cont
        print(f"Média de duração dos filmes: {media:.2f} minutos")


while True:
    menu()
    escolha = input("\nQual opção deseja escolher: ").strip()

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
        media_duracao()
    elif escolha == "6":
        print("Encerrando sistema...")
        break
    else:
        print("Opção inválida, digite novamente.")