dia = int(input())
if (dia < 1 or dia > 31):
    print('Dia inexistente')
else:  
    mes = int(input())  
    if (mes < 1 or mes > 12):
        print('Mês inexistente')
    elif (dia >= 30 and mes == 2):
        print("Esse dia não existe nesse mês")
    else:
        ano = int(input())
        meses_com_31 = [1, 3, 5, 7, 8, 10, 12]
        meses_com_30 = [4, 6, 9, 11]
        

        max_fev = 28 if ano % 4 != 0 or (ano % 100 == 0 and ano % 400 !=0) else 29

        if (ano <1990 or ano >2020):
            print('Ano inexistente')

        elif mes in meses_com_31:
            print('Data Validada')


        elif mes in meses_com_30:
            print('Data Validada')

        elif mes == 2 and dia <= max_fev:
            print('Data Validada')


        else:
            print('Data inválida')
