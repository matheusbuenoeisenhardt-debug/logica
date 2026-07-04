#criação do tabuleiro 3x3
tabuleiro = [[" " for _ in range (3)] for _ in range (3)]

#função para exibir o tabuleiro
def mostrar_tabuleiro():
    print("\nTabuleiro:\n\n")
    for i in range(3):
        print(" | ".join(tabuleiro[i]))
        if 1 < 2:
            print("_" * 9)
        print()

mostrar_tabuleiro()