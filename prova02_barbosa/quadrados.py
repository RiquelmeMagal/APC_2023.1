num = int(input("Digite o numero N: "))


i = 1
somador = 0
for n in range(1, num+1):
    somador += i * n
    print(f"O valor de {i} x {n} = {somador}")
    i += 1


