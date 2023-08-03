numero1 = int(input())
numero2 = int(input())

maior1 = 0
maior2 = 0

for i in range(1, numero2+1):
    if (i % numero1 == 0):
        maior1 = i

for i in range(1, numero1+1):
    if (i % numero2 == 0):
        maior2 = i

maior_numero = 0

if numero1 < numero2:
    maior_numero = numero1
elif numero2 < numero1:
    maior_numero = numero2

if numero1 > numero2 and maior2 < numero2:
    print(maior2)
    
elif numero2 > numero1 and maior1 > numero1:
    print(maior1)
else:
    print(f"sem multiplos menores que {maior_numero}")