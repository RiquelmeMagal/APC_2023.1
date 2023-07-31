while True:
    entrada = float(input())
    if entrada == -1:
        break
    else:
        if (entrada < 7):
            print('ACIDA')
        elif (entrada > 7):
            print('BASICA')
        else:
            print('NEUTRA')