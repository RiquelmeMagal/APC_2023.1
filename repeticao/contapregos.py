pregos = 12
preco = 7.89

while True:
    numero = int(input())
    if numero % 2 != 0:
        break
    pregos = pregos - numero
    if pregos <= 0:
        pregos = 12
        preco = preco + 7.89
    elif pregos < numero:
        pregos = pregos + 12
        pregos = pregos - numero
        preco = preco + 7.89


print(f"{preco:.2f}")
print(pregos)
