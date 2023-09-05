texto = input()
contador = {}

for letra in texto:
    if letra in contador:
        contador[letra] += 1
    else:
        contador[letra] = 1

for letra in sorted(contador, reverse=True):
    print(letra, contador[letra])
