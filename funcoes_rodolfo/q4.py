lista1 = {1,2,3,4,5,6,7}
lista2 = {4,5,6,7,8,9,10}

def uniao(lista1,lista2):
    lista3 = lista1.union(lista2)
    return lista3

#print(list(set(uniao(lista1,lista2))))

def copiar_sem_repeticao(lista):
    nova_lista = []
    for item in lista:
        if item not in nova_lista:
            nova_lista.append(item)
    return nova_lista

def imprimir_lista(lista):
    for item in lista:
        print(item)


lista_original = [1, 2, 3, 2, 4, 1, 5, 4, 6, 7, 8, 5]

lista_sem_repeticao = copiar_sem_repeticao(lista_original)

print("Lista original:")
imprimir_lista(lista_original)

print("Lista sem repetição:")
imprimir_lista(lista_sem_repeticao)
