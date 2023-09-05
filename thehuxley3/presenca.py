numero = int(input())

conjunto = set()
for _ in range(numero):
    entrada = input()
    conjunto.add(entrada)

print(len(conjunto))
