lista = [9,5,1,3,6,4,10,7]


numero_a_ser_procurado = -8

numero_mais_proximo = lista[0]

diferenca_mais_proxima = abs(numero_a_ser_procurado - numero_mais_proximo)
print(diferenca_mais_proxima)

for numero in lista:
    diferenca_atual = abs(numero_a_ser_procurado - numero)
    if diferenca_atual < diferenca_mais_proxima:
        diferenca_mais_proxima = diferenca_atual
        numero_mais_proximo = numero

print(f"O número mais próximo de {numero_a_ser_procurado} é {numero_mais_proximo}, a diferença é {diferenca_mais_proxima}")