#Escreva um programa que possui uma função que recebe uma lista e diz qual a soma máxima entre dois elementos da lista

lista_numeros = [1,2]
def maior_soma(lista):
    if len(lista) < 2:
        return "Lista menor < 2."
    maior = lista_numeros[0] + lista_numeros[1]
    for i in lista_numeros:
        for k in lista_numeros:
            if (i + k > maior) and (i != k):
                maior = i + k
    return maior

print(maior_soma(lista_numeros))