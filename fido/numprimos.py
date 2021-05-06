print("Bem-vindo!!!")
print("Esse programa apresenta os números primos contidos numa lista de -4 a 29!")
print("\n")

primos =[]
print('lista de números: \n', list(range(-4, 30, 1)))
for x in range(-4, 30, 1):
    cont = 0
    for y in range(1, x+1):
        if(x % y == 0):
            cont += 1
    if cont == 2:
        primos.append(x)

print('números primos : \n', primos)

