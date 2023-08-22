lista_produtos = []


for i in range(15):
    produto = int(input("Digite o peso: "))
    lista_produtos.append(produto)


for i in range(len(lista_produtos)):
    if (lista_produtos[i] > 92) or (lista_produtos[i] < 88):
        print(f"Produto no índice {i} está fora do padrão")

