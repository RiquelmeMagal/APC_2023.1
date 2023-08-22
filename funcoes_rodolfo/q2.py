#Escreva um programa que possui uma função que recebe uma lista e um valor e verifica se existe o valor na lista

def existe(lista, valor):
    for i in lista:
        if valor == i:
            return "existe"
    return -1

lista1 = [10, 8, 1, 3, 5, 7, 20, 0]
lista2 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
lista3 = [10, 9, 8, 7, 6, 5, 2, 1]


print(existe(lista1, 1))
print(existe(lista2, 20))
print(existe(lista3, 50))
