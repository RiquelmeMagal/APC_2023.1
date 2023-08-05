

Numero_de_votantes = 0
Total_A = 0
Total_B = 0
Total_C = 0
Total_brancos = 0
Total_nulos = 0
Validos = 0
Candidato_mais_votado = 0
Eleicao_valida = False
Segundo_turno = False


while True:
    secao = int(input())
    if secao == 0:
        break

    candidato_a = int(input())
    Total_A += candidato_a

    candidato_b = int(input())
    Total_B += candidato_b

    candidato_c = int(input())
    Total_C += candidato_c

    brancos = int(input())
    Total_brancos += brancos

    nulos = int(input())
    Total_nulos += nulos

Validos = Total_A + Total_B + Total_C
Numero_de_votantes = Total_A + Total_B + Total_C + Total_brancos + Total_nulos

if Total_A > Total_B and Total_A > Total_C:
    Candidato_mais_votado = "A"
elif Total_B > Total_A and Total_B > Total_C:
    Candidato_mais_votado = "B"
elif Total_C > Total_A and Total_C > Total_B:
    Candidato_mais_votado = "C"

else:
    Candidato_mais_votado = ''



if Validos > (Total_brancos + Total_nulos):
    Eleicao_valida = True
else:
    Eleicao_valida = False

if Total_C > (Total_A + Total_B) and Eleicao_valida == True:
    Segundo_turno = False
elif Total_B > (Total_A + Total_C) and Eleicao_valida == True:
    Segundo_turno = False
elif Total_A > (Total_B + Total_C) and Eleicao_valida == True:
    Segundo_turno = False
else:
    if Eleicao_valida == False:
        Segundo_turno = False
    else:
        Segundo_turno = True


print(f"Numero de votantes: {Numero_de_votantes}")
print(f"Total A: {Total_A}")
print(f"Total B: {Total_B}")
print(f"Total C: { Total_C}")
print(f"Brancos: {Total_brancos}")
print(f"Nulos: {Total_nulos}")
print(f"Validos: {Validos}")
print(f"Candidato mais votado: {Candidato_mais_votado}")
print(f"Eleicao valida? {Eleicao_valida}")
print(f"Segundo turno? {Segundo_turno}")
