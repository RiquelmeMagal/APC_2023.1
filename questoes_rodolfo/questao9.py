palavra = input("Digite uma palavra: ")

caracter = input("Digite um caracter: ")


contador = 0
for i in palavra:
    if i == caracter:
        contador += 1

print(contador)