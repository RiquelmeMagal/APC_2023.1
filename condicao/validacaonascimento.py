def data_valida(dia, mes, ano):
    meses_com_31 = [1, 3, 5, 7, 8, 10, 12]
    meses_com_30 = [4, 6, 9, 11]

    if mes < 1 or mes > 12:
        return False

    if mes == 2:
        max_fev = 28 if ano % 4 != 0 or (ano % 100 == 0 and ano % 400 != 0) else 29
        if dia < 1 or dia > max_fev:
            return False
    elif mes in meses_com_31:
        if dia < 1 or dia > 31:
            return False
    elif mes in meses_com_30:
        if dia < 1 or dia > 30:
            return False

    return True

dia = input("Digite o dia: ")

if dia == '':
    print('Dia inexistente')
else:
    dia = int(dia)
    if dia < 1 or dia > 31:
        print('Dia inexistente')
    else:
        mes = input("Digite o mês (ou deixe vazio): ")

        if mes == '':
            print('Mês inexistente')
        else:
            mes = int(mes)
            if mes < 1 or mes > 12:
                print('Mês inexistente')
            else:
                if not data_valida(dia, mes, 2000):  # Vamos usar 2000 como exemplo de um ano válido
                    print("Esse dia não existe nesse mês")
                else:
                    ano = input("Digite o ano (ou deixe vazio): ")

                    if ano == '':
                        print('Ano inexistente')
                    else:
                        ano = int(ano)

                        if not data_valida(dia, mes, ano):
                            if mes == 2 and dia == 29 and not (ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)):
                                print("Esse ano não é bissexto")
                            else:
                                print('Data inválida')
                        elif ano < 1900 or ano > 2020:
                            print('Ano inexistente')
                        else:
                            print('Data Validada')
