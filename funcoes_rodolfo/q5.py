def calcular_nota(nota, min_nota, max_nota):
    nota_calculada = ((nota - min_nota) / (max_nota - min_nota)) * 10
    return nota_calculada

num_alunos = int(input("Quantidade de alunos: "))
notas = []

for i in range(num_alunos):
    nota = float(input(f"Informe a nota do aluno {i + 1}: "))
    notas.append(nota)

max_nota = max(notas)
min_nota = min(notas)

print("\nNotas calculadas:")
for i, nota in enumerate(notas):
    nota_calculada = calcular_nota(nota, min_nota, max_nota)
    print(f"Aluno {i + 1}: Nota original = {nota:.2f}, Nota calculada = {nota_calculada:.2f}")

