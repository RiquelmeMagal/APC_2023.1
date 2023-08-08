lista = []


quantidade = int(input("Digite a quantidade de números: "))

for i in range(quantidade):
    lista.append(int(input("Digite um número: ")))

numero = int(input("Digite um número da lista: "))

if numero in lista:
    for i in lista:
        if i > numero:
            print(i)
else:
    print("Número não está na lista.")
