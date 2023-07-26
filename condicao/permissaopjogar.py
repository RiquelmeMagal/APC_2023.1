lista = ['azar', 'mmorpg', 'moba', 'casual']

idade = int(input())
tipo_jogo = str(input())

if (idade < 0 or idade > 130):
    print("Idade invalida.")
else:
    if (tipo_jogo not in lista):
        print("Jogo invalido.")
    elif (idade >= 21 and tipo_jogo == 'azar'):
        print("Pode entrar!")
    elif (idade >= 14 and tipo_jogo == "mmorpg"):
        print("Pode entrar!")
    elif (idade >= 10 and tipo_jogo == 'moba'):
        print("Pode entrar!")
    elif (idade >= 0 and idade <= 130 and tipo_jogo == 'casual'):
        print("Pode entrar!")
    else:
        print("Volte daqui há alguns anos.")
