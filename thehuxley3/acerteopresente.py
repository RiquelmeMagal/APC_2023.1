# dicionario = {}
# dicionario['iara'] = ['sereia', 'rio', 'lenda']

# print('sim' if 'sereia' in dicionario['iara'] else 'no')

numero = int(input())
dicionario_presentes = {}

while True:
    for i in range(numero):
        presente = input().split()
        if presente[0] == "FIM":
            break
        else:
            presente_ = [presente[i] for i in range(1, len(presente))]
            dicionario_presentes[presente[0]] = presente_
    
    while True:
        presente = input().split()
        if presente[0] == "FIM":
            break
        if presente[1] in dicionario_presentes[presente[0]]:
            print("Uhul! Seu amigo secreto vai adorar")
        else:
            print("Tente Novamente!")
    if  presente[0] == "FIM": 
        break
