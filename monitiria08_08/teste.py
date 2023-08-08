numeros = [1,3,5,8,6,7,4]

n1 = 5
n2 = 8

i = 0
while i < len(numeros)-1 and n1 != numeros[i] or n2 != numeros[i+1]:
    i+=1
if i == len(numeros)-1:
    print('Não achou')
else:
    print('Achou')