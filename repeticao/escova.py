inteiro = int(input())

soma = 0
cont = 0
for i in range(inteiro):
    cont = cont + 1
    if cont == 3:
        cont = 0
    else:
        soma += 2.2

print(f"{soma:.2f}")