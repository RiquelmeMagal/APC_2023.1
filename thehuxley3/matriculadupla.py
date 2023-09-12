# Ler as matrículas dos alunos de Programação II
matriculas_programacao_ii = input().split()
matriculas_programacao_ii = [int(x) for x in matriculas_programacao_ii]

# Ler as matrículas dos alunos de Programação III
matriculas_programacao_iii = input().split()
matriculas_programacao_iii = [int(x) for x in matriculas_programacao_iii]

# Encontrar a interseção entre as duas listas de matrículas
interseccao = [matricula for matricula in matriculas_programacao_ii if matricula in matriculas_programacao_iii]

# Imprimir a interseção com espaço em branco e final de linha após o último número
for i, matricula in enumerate(interseccao):
    if i == len(interseccao) - 1:
        print(matricula)
    else:
        print(matricula, end=' ')
