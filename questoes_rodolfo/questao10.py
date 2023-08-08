palavra = input("Digite uma palavra: ")


contador_vogais = 0
for i in palavra:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        contador_vogais = contador_vogais + 1

print(contador_vogais)
    