numero = int(input("Digite um número: "))

count = 1

for i in range(1, numero + 1):
    count *= i

print(count)