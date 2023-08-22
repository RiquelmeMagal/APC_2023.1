def verifica_substring(palavra_a, palavra_b):
    if palavra_b in palavra_a:
        return True
    else:
        return False


palavra_a = input("Digite a primeira palavra: ")
palavra_b = input("Digite a segunda palavra: ")

if verifica_substring(palavra_a, palavra_b):
    print(f"{palavra_b} é uma substring de {palavra_a}.")
else:
    print(f"{palavra_b} não é uma substring de {palavra_a}.")

