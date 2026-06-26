c = float(input("Digite a temperatura em graus Celsius: "))
f = (c * 9/5 + 32)
k = (c + 273)
calculo = int(input('Escolha a converção: 1 = Farenheit, 2 = Kelvin: ' ))
if calculo == 1:
  print(f"A conversão da temperatura em graus Farenheit fica: {f: .1f}° Farenheit")
elif calculo == 2:
  print(f"A conversão da temperatura em graus Kelvin fica: {k: .1f}° Kelvin")
else:
  print("Resposta invalida")