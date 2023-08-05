lista = [1, 3, 8, 4, 6, 10, 8]

n = 6

i = 0

while (i < len(lista) and lista[i] != n):
    i = i + 1


if (i == len(lista)):        
    print("Não achou")
else:
    print("Achou na posição: ", i)