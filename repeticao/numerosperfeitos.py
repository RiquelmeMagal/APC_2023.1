
def soma_divisores(num):
    soma = 0
    for i in range(1, num):
        if num % i == 0:
            soma += i
    return soma

def lista_numeros_perfeitos(n):
    numeros_perfeitos = []
    for num in range(1, n):
        if soma_divisores(num) == num:
            numeros_perfeitos.append(num)
    return numeros_perfeitos


num = int(input())


numeros_perfeitos = lista_numeros_perfeitos(num)


for perfeito in numeros_perfeitos:
    print(perfeito)
