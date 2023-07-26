# Entrada de dados
idade_aluno = int(input())
nota_prova1 = float(input())
nota_prova2 = float(input())
nota_reposicao = float(input())

media = (nota_prova1 + nota_prova2) / 2


if (idade_aluno >= 18):
    media_final = (media * 6 + nota_reposicao * 3) / 9
else:   
    if (nota_prova1 < 7 or nota_prova2 < 7):
 
        menor_nota = min(nota_prova1, nota_prova2)
        if (menor_nota == nota_prova1):
            nova_nota = nota_reposicao
            media_final = (nota_prova2 + nova_nota) / 2
        else:
            nova_nota = nota_reposicao
            media_final = (nota_prova1 + nova_nota) / 2

    media_final = (nota_prova1 + nota_prova2) / 2

if (media_final >= 5.5 and nota_prova1 >= 4 and nota_prova2 >= 4 and nota_reposicao >= 4):
    print("Aprovado")
else:
    print("Reprovado")
