lista_numeros = []


quantidadeNumerosLista = int(input("Digite a quantidade de números que deseja inserir na lista: "))


for numero in range(quantidadeNumerosLista):
    lista_numeros.append(int(input("Digite um número: ")))
    

for numero in lista_numeros:
    if numero < 0:
        print(numero)