print("Bem-vindo!!!")
print("Esse programa é para identificar se existe números repetidos no array!")
print("\n")

numeros = [10, 10, 30, 40, 50, 60, 70, 80, 90, 100]

repetidos = []
nao_repetidos = []

for n in numeros:
    if n not in nao_repetidos:
        nao_repetidos.append(n)
    else:
        repetidos.append(n)
print('Números do array:')
print(numeros)

if(bool(repetidos)==True):
    print("Sim existe números repetidos!")
else:
    print("Não existe números repetidos!")


