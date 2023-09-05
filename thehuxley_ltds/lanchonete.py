cardapio = [

]
quantidade = int(input())
for i in range(quantidade):
    id = int(input())
    nome = input()
    preco = float(input())
    cardapio.append({id:[nome,preco]})

print(cardapio)

while True:
    count = 0
    id = int(input())

    if (id == 0):
        break

    quantidade = int(input())

    if (quantidade < 0):
        break

    
