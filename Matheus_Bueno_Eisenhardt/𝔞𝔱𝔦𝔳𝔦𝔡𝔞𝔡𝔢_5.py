nr = int(input("qual numero deseja saber a tabuada?"))
x = 1
for i in range(10):
  if x <= 10:
    print(f"{nr} x {x} = {nr * x}")
    x += 1
  else:
    break
