lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
maior_valor_lido = None
soma_diagonal = 0

for i in range(len(lista)):
    for j in range(len(lista[i])):
        valor = int(input(f"Digite um valor para lista[{i}][{j}]: "))
        lista[i][j] = valor

        if maior_valor_lido is None or valor > maior_valor_lido:
            maior_valor_lido = valor

        if i == j:
            soma_diagonal += valor

# Determine o delta com base no maior valor lido
delta = 1 if maior_valor_lido > 0 else -1 if maior_valor_lido < 0 else 0

total = 0
soma = 0

for linha in lista:
    soma += sum(linha)
    total += len(linha)

media = soma / total

print(f"Maior valor lido: {maior_valor_lido}")
print(f"Delta: {delta}")
print(f"Soma da diagonal principal: {soma_diagonal}")
print(f"Média dos valores na matriz: {media:.2f}")
