lista_sexo = []
lista_servicos = []
lista_preco = []
while True:
    sexo = input()
    if (sexo.upper() != 'M') and (sexo.upper() != 'F'):
        break
    servico = input()
    lista_sexo.append(sexo.upper())
    lista_servicos.append(servico.upper())
    if (sexo.upper() == 'M') and (servico.upper() == 'CORTE'):
        lista_preco.append(25)
    elif (sexo.upper() == 'M') and (servico.upper() == 'BARBA'):
        lista_preco.append(15)
    elif sexo.upper() == 'F' and servico.upper() == 'CORTE':
        lista_preco.append(40)
    elif sexo.upper() == 'F' and servico.upper() == 'PENTEADO':
        lista_preco.append(50)
    elif sexo.upper() == 'F' and servico.upper() == 'MAQUIAGEM':
        lista_preco.append(70)

lista_unida = list(zip(lista_sexo, lista_servicos, lista_preco))

faturamento = 0
for i in lista_unida:
    faturamento += i[2]
homens = 0
for i in lista_unida:
    homens += i[0].count('M')
barba = 0
corte = 0
for i in lista_unida:
    barba += i[1].count('BARBA')
    corte += i[1].count('CORTE')
if (barba > corte) and homens > 0:
    print('BARBA')
    print(f'{faturamento:.2f}')
elif (corte > barba) and homens > 0: 
    print('CORTE')
    print(f'{faturamento:.2f}')
else:
    print("AMBOS")
    print(f'{faturamento:.2f}')