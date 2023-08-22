def calcular_mdc(a,b):
    while b:
        a,b = b, a % b
    return a


print(calcular_mdc(6,12))



def calcular_mdc_(num1, num2):
    maior_valor = 0
    if num1 < num2:
        maior_valor = num1
    elif num2 < num1:
        maior_valor = num2 
    else:
        maior_valor = num2
    mdc = 0
    for i in range(1, maior_valor +1):
        if (num1 % i == 0) and (num2 % i == 0):
            if i > mdc:
                mdc = i
                
                
    return mdc
numero1 = int(input())
numero2 = int(input())
mdc = calcular_mdc_(numero1,numero2)
print(f"MDC={mdc}")