largura_maxima = 45
comprimento_maximo = 56
altura_maxima = 25

largura = float(input())
comprimento = float(input())
altura = float(input())

if (largura <= largura_maxima) and (comprimento <= comprimento_maximo) and (altura <= altura_maxima):
    print("PERMITIDA")
else:
    print("PROIBIDA")