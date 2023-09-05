dicionario = []
while True:
    entrada = input().split()
    if entrada[0] == "*":
        break
    else:
        dicionario.append(entrada)

gabarito = input()

lista_2 = []
for i in dicionario:
    lista_2.append(i[1])

total_alunos = len(lista_2)
total_acertos = [0] * len(gabarito)

for aluno_resposta in lista_2:
    for i, resposta in enumerate(aluno_resposta):
        if resposta == gabarito[i]:
            total_acertos[i] += 1

maior_acertos = max(total_acertos)
menor_acertos = min(total_acertos)
media_acertos = sum(total_acertos) / len(gabarito) / total_alunos  # Correção na fórmula da média

print("Maior:", maior_acertos)
print("Menor:", menor_acertos)
print("Media:", format(media_acertos, '.2f'))
