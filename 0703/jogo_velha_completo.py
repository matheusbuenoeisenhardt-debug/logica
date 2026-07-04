#criação do tabuleiro 3x3
tabuleiro = [[" " for _ in range (3)] for _ in range (3)]

#função para exibir o tabuleiro
def mostrar_tabuleiro():
    print("\nTabuleiro:\n")
    for i in range(3):
        print(" | ".join(tabuleiro[i]))
        if i < 2: # Imprime a linha divisória apenas entre as linhas do tabuleiro
            print("---------")
    print() # Linha em branco para espaçamento após o tabuleiro

# Função para verificar vitória
def verificar_vitoria(jogador):
    # Verificar linhas
    for i in range(3):
        if all(tabuleiro[i][j] == jogador for j in range(3)):
            return True
    # Verificar colunas
    for j in range(3):
        if all(tabuleiro[i][j] == jogador for i in range(3)):
            return True
    # Verificar diagonais
    if (tabuleiro[0][0] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][2] == jogador) or \
       (tabuleiro[0][2] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][0] == jogador):
        return True
    return False

# A chamada inicial de mostrar_tabuleiro() foi movida para dentro da função jogar para um fluxo mais lógico

#função principal do jogo
def jogar():
    jogador_atual = "X"
    jogadas = 0

    while True:
        mostrar_tabuleiro()

        print(f"Jogador {jogador_atual}, é a sua vez.")
        try:
            linha = int(input("Informe a linha (0 a 2): "))
            coluna = int(input("Informe a coluna (0 a 2): "))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
            continue

        # Verifica se a entrada está dentro do intervalo válido
        if not (0 <= linha <= 2 and 0 <= coluna <= 2):
            print("Entrada inválida. A linha e a coluna devem ser entre 0 e 2.")
            continue

        #verifica se a posição está livre
        if tabuleiro[linha][coluna] != " ":
            print("Posição já ocupada. Tente novamente.")
            continue

        #faz a jogada
        tabuleiro[linha][coluna] = jogador_atual
        jogadas += 1

        #verificar vitória
        if verificar_vitoria(jogador_atual):
          mostrar_tabuleiro()
          print(f"Parabéns! O jogador {jogador_atual} venceu o jogo!")
          break # Finaliza o jogo após a vitória

        #verificar empate
        if jogadas == 9:
          mostrar_tabuleiro()
          print("O jogo terminou em empate!")
          break # Finaliza o jogo em caso de empate

        #alternar jogador (garantindo consistência 'X' e 'O')
        jogador_atual = "O" if jogador_atual == "X" else "X"

# Inicia o jogo
jogar()