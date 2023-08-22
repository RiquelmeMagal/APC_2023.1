quantidades_entrevistados = int(input("Quantos entrevistados? "))

lista_peso = []
lista_altura = []

for i in range(quantidades_entrevistados):
    peso = float(input("Digite o peso: "))
    altura = float(input("Digite a altura: "))
    lista_peso.append(peso)
    lista_altura.append(altura)

for i in range(len(lista_peso)):
    if (lista_peso[i] / lista_altura[i] ** 2 <= 18.49):
        print("Abaixo do peso")
    elif (lista_peso[i] / lista_altura[i] ** 2 >= 18.5) and (lista_peso[i] / lista_altura[i] ** 2 <= 24.99):
        print("Peso normal")
    elif (lista_peso[i] / lista_altura[i] ** 2 >= 25) and (lista_peso[i] / lista_altura[i] ** 2 <= 29.99):
        print("Acima do peso")
    elif (lista_peso[i] / lista_altura[i] ** 2 >= 30):
        print("Obesidade")