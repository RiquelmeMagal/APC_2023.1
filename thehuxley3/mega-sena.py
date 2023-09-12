# Função para contar os acertos de uma aposta
def contar_acertos(aposta, numeros_sorteados):
    return len(set(aposta) & set(numeros_sorteados))

# Dicionário para armazenar as apostas dos amigos
apostas = {}

# Lê as apostas dos amigos até encontrar a linha com a string "FIM"
while True:
    linha = input().split()
    if linha[0] == "FIM":
        break
    nome = linha[0]
    numeros_apostados = [int(num) for num in linha[1:]]
    apostas[nome] = numeros_apostados

# Lê os números sorteados
numeros_sorteados = [int(num) for num in input().split('-')]

# Calcula os acertos de cada amigo e armazena em um dicionário
acertos_amigos = {}
for nome, aposta in apostas.items():
    acertos = contar_acertos(aposta, numeros_sorteados)
    acertos_amigos[nome] = acertos

# Ordena a lista de amigos por número de acertos e, em caso de empate, por nome
amigos_ordenados = sorted(acertos_amigos.items(), key=lambda x: (-x[1], x[0]))

# Imprime o resultado
for amigo, acertos in amigos_ordenados:
    print(f'{amigo} {"+" * acertos}')
