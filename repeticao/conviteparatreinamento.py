quantidade = int(input())
pontuacaoMinina = float(input())

lista = []

for i in range(quantidade*2):
    lista.append(float(input()))

lista2 = lista[0:quantidade]
lista3 = lista[quantidade:]

passaram = 0
for i in range(quantidade):
    if lista2[i] + lista3[i] >= pontuacaoMinina:
        passaram += 1
        
print(passaram)