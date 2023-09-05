# Número de pessoas
n = int(input())

#Lista para armazenar informações das pessoas
lista = []

#Loop para ler as entradas e criar dicionários para cada pessoa
for _ in range(n):
    nome = input()
    id = int(input())
    level = int(input())
    vida = int(input())
    ataque = int(input())
    defesa = int(input())
    
    
    adicionar = {
        "nome": nome,
        "id": id,
        "level": level,
        "vida": vida,
        "ataque": ataque,
        "defesa": defesa
    }
    
    lista.append(adicionar)

#Iterar sobre a lista e imprimir as saídas desejadas
for _ in lista:
    print("Nome:", _["nome"])
    print("ID:", _["id"])
    print("Level:", _["level"])
    print("Vida:", _["vida"])
    print("Ataque:", _["ataque"])
    print("Defesa:", _["defesa"])
    
