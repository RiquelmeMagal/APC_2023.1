lista = [10,5,9,3,7,2,1,4]


numero_a_ser_buscado = 50

numero_mais_proximo = lista[0]
diferenca_proxima = abs(numero_a_ser_buscado - numero_mais_proximo)



for numero in lista:
    diferenca_atual = abs(numero_a_ser_buscado - numero)
    if diferenca_atual < diferenca_proxima:
        diferenca_proxima = diferenca_atual
        numero_mais_proximo = numero

print(f"O número a ser buscado foi o {numero_a_ser_buscado}, o mais próximo foi o {numero_mais_proximo}, a diferença foi de {diferenca_proxima}")