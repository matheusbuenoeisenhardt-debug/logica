nota1 = float(input("digite sua 1° nota: "))
nota2= float(input("digite sua 2 nota: "))
nota3= float(input("digite sua 3 nota: "))
nota4= float(input("digite sua 4 nota: "))

soma = nota1 + nota2 + nota3 + nota4

media = soma / 4

if media < 5:
    print(f"a media foi: {media}, portanto o resultado é: reprovado")

elif media >= 5 and media < 7:
    print(f"a media foi: {media}, portanto o resultado é: exame")

else:
    print(f"a media foi: {media}, portanto o resultado é: aprovado")