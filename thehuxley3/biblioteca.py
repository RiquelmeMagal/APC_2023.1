n = int(input())

lista_livros = []

for i in range(n):
    livro = input().replace(" ", "").replace("|", " ").split()

    lista_livros.append(livro)

livro_recebido = input().replace(" ", "").replace("|", " ").split()

verdadeiro = False

for i in lista_livros:
    if livro_recebido == i:
        verdadeiro = True
        break

if verdadeiro:
    print("Sim")
else:
    print("Não")   

