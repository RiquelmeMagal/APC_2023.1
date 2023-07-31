lista = []

quantidade = int(input("Digite a quantidade de números: "))

for i in range(1, quantidade + 1):
    
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    altura = float(input("Digite a altura: "))
    peso = float(input("Digite o peso: "))

    imc = peso / (altura ** 2)

    lista.append({"nome": nome, "idade": idade, "altura": altura, "peso": peso, "imc": imc})

for i in lista:
    print(i['nome'], i['idade'], i['altura'], i['peso'], i['imc'])