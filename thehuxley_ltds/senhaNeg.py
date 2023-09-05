dicionario = {
    "0": "6",
    "1": "7",
    "2": "9",
    "3": "8",
    "4": "A",
    "5": "2",
    "6": "B",
    "7": "F",
    "8": "1",
    "9": "C",
    "A": "0",
    "B": "D",
    "C": "E",
    "D": "3",
    "E": "5",
    "F": "4",
}
quantidade = int(input())

palavras = [

]
lista = []

for i in range(quantidade):
    palavras.append(input(""))

for palavra in palavras:
    novaPalavra = ''
    if palavra.isalnum() and palavra.isupper():
        for char in palavra:
            if char in dicionario:
                novaPalavra += dicionario[char]
            else:
                novaPalavra += char
        lista.append(novaPalavra)
    else:
        print("Alguma senha eh invalida!")

for _ in lista:
    print(f"-{_}", end ='')

soma = 0
for _ in lista:
    for __ in _:
        soma += 1
if soma > 0:
    print(f" {soma}")
