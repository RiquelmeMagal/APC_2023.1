lista = []


quantidade = int(input("Digite a quantidade de números: "))

for i in range(quantidade):
    lista.append(int(input("Digite um número: ")))

media = sum(lista) / len(lista)

for i in lista:
    if i < media:
        print(i)
