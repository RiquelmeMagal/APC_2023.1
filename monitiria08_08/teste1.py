numeros = [1,3,5,8,6,7,4]

n = -10

menor_distancia = abs(n - numeros[0]) 



mais_proximo = numeros[0] #1
for num in numeros:
    distancia = abs(n - num)
    print(distancia, num)
    if distancia < menor_distancia:
        menor_distancia = distancia
        mais_proximo = num
print(f'O valor mais próximo de {n} é {mais_proximo}')