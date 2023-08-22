"""
Você está implementando um sistema de taxi por aplicativo. Quando um usuário solicita um taxi,
o aplicativo carrega a localização deste usuário e precisa encontrar o taxi mais próximo para realizar a
chamada. Para calcular a distância, o aplicativo utiliza a distância euclidiana, como descrito abaixo. Faça
um programa que recebe como entradas a localização atual de um usuário (x,y) e as lista de localizações
dos taxis disponíveis taxisx = [x¹,x²,...,xⁿ], taxisy = [y¹,y²,...,yⁿ], e imprima na tela o taxi mais próximo.

d((xᵢ, yᵢ),(xj , yⱼ ) = raiz de -> (xᵢ − yⱼ )² + (yᵢ − yⱼ )²


Exemplo:

x = 10, y = 8

taxisx = [21, 40, 35, 17, −42, 82, 60, −1, −15, 25, 29, 0]
taxisy = [25, 30, −1, 45, −20, 60, 0, 26, −10, 52, 36, −1]

saída: 11

"""

x_taxi = [21, 40, 35, 17, -42, 82, 60, -1, -15, 25, 29, 0]
y_taxi = [25, 30, -1, 45, -20, 60, 0, 26, -10, 52, 36, -1]

x_usuario = -1
y_usuario = 2

for i in range(len(x_taxi)):
    x = (x_taxi[i] - x_usuario) ** 2
    y = (y_taxi[i] - y_usuario) ** 2
    soma = x + y
    raiz = soma ** (1/2)

    if i == 0:
        menor_distancia = raiz
        indice_menor_distancia = i
    else:
        if raiz < menor_distancia:
            menor_distancia = raiz
            indice_menor_distancia = i

    #print(f'Táxi posição: ({x_taxi[i]}, {y_taxi[i]}) - distância: {raiz:.2f}')

print(indice_menor_distancia)




x_taxi = [21, 40, 35, 17, -42, 82, 60, -1, -15, 25, 29, 0]
y_taxi = [25, 30, -1, 45, -20, 60, 0, 26, -10, 52, 36, -1]

lista = list(zip(x_taxi, y_taxi))

x = -1
y = 2
absoluto = abs(lista[0][0] - x) + abs(lista[0][1] - y)
ponto = 0  # Índice do ponto mais próximo

for i, ponto_atual in enumerate(lista):
    diferenca = abs(ponto_atual[0] - x) + abs(ponto_atual[1] - y)
    if diferenca < absoluto:
        absoluto = diferenca
        ponto = i

print("Menor diferença absoluta:", absoluto)
print("Índice do ponto mais próximo:", ponto)
print("Coordenadas do ponto mais próximo:", lista[ponto])
