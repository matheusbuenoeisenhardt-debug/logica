lista = []
def menu():
    print("digite uma das seguintes opções: ")
    print("1 - Adicionar um número à lista")
    print("2 - Remover um número da lista")
    print("3 - Exibir a lista")
    print("4 - Exibir a soma dos números da lista")
    print("5 - Exibir a média dos números da lista")
    print("6 - exibir o maior número da lista")
    print("7 - Sair")

while True:

    menu()

    escolha = int(input("\nqual opção deseja escolher? \n"))

    if escolha == 1:
        numero = float(input("digite um numero que voce deseja adicionar na lista: "))
        lista.append(numero)
        print(f"o numero {numero} foi adicionado na lista com sucesso\n")

    elif escolha == 2:
        numero = float(input("digite o numero que voce deseja remover da lista: "))
        if numero in lista:
            print(f"o numero {numero} foi removido da lista com sucesso\n")
            lista.remove(numero)
        else:
            print("numero não encontrado na lista")

    elif escolha == 3:
        print(f"os números presentes na lista são: {lista}\n")

    elif escolha == 4:
        soma = sum(lista)
        print(f"a soma dos números da lista é: {soma}\n")

    elif escolha == 5:
        soma = sum(lista)
        media = soma / len(lista)
        if len(lista) > 0:
            print(f"a media dos números da lista é: {media}\n")

    elif escolha == 6:
        maior = None
        for numero in lista:
            if len(lista) > 0:
                if maior is None or maior < numero:
                    maior = numero
            print(f"o maior número da lista é: {maior}\n")

    elif escolha == 7:
        print("encerrando programa.")
        break