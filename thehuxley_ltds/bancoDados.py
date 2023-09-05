# Número de pessoas
n = int(input())

#Lista para armazenar informações das pessoas
pessoas = []

#Loop para ler as entradas e criar dicionários para cada pessoa
for _ in range(n):
    idade = int(input())
    nome = input()
    sexo = input()
    estado_civil = input()
    quantidade_amigos = int(input())
    quantidade_fotos = int(input())
    
    pessoa = {
        "idade": idade,
        "nome": nome,
        "sexo": sexo,
        "estado_civil": estado_civil,
        "quantidade_amigos": quantidade_amigos,
        "quantidade_fotos": quantidade_fotos
    }
    
    pessoas.append(pessoa)

#Iterar sobre a lista e imprimir as saídas desejadas
for pessoa in pessoas:
    print("Idade:", pessoa["idade"])
    print("Nome:", pessoa["nome"])
    print("Sexo:", pessoa["sexo"])
    print("Estado Civil:", pessoa["estado_civil"])
    print("Numero de amigos:", pessoa["quantidade_amigos"])
    print("Numero de fotos:", pessoa["quantidade_fotos"])
    print()
