#Escreva um programa que possui uma função “maior”, que recebe uma lista e devolve o maior elemento na lista

def maior(lista):
    maior_elemento = lista[0]
    for i in lista:
        if i > maior_elemento:
            maior_elemento = i
    return maior_elemento
    #return max(lista)


lista1 = [10, 8, 1, 3, 5, 7, 20, 0]
lista2 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
lista3 = [10, 9, 8, 7, 6, 5, 2, 1]


print(maior(lista1))
print(maior(lista2))
print(maior(lista3))

