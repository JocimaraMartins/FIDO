print("Bem-vindo!!!")
print("Esse programa apresenta um array de números na ordem crescente e decrescente!")
print("\n")

numeros = [4, 68, 1, 87, 34, 0, 99, 7, 88, 56, 9, 100, 10]
print(f'Os valores na ordem que foram inseridos: {numeros}')

numeros.sort()
print(f'Os valores na ordem crescente são: {numeros}')

numeros.sort(reverse=True)
print(f'Os valores na ordem decrescente são: {numeros}')



