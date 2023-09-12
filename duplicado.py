lista = [
    1,2,3,4,5,5,6,6,7,7
         ]

def copiar_lista_sem_repetidos(lista):
    return [valor for valor in lista if lista.count(valor) == 1]


copia_lista = copiar_lista_sem_repetidos(lista)

print(lista)
print(copia_lista)