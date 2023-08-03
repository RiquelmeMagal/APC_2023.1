
lista_geral = []

while True:
    entrada_portugues = float(input())
    if entrada_portugues < 0:
        break
    entrada_matematica = float(input())
    entrada_redacao = float(input())
    
    lista_geral.append([entrada_portugues, entrada_matematica, entrada_redacao])
    
    

def aprovados():
    contador = 0
    for i in lista_geral:
        if (i[0] * 100 / 50) >= 80 and (i[1] * 100 / 35 >= 60) and (i[2] >= 7):
            contador += 1
    return contador

print(aprovados())

