with open("nova_senha.txt", "w") as arquivo:
    arquivo.write("Essa é a minha nova senha")
    arquivo.write("123456")


with open("nova_senha.txt", "r") as arquivo:
    print(arquivo.readline())
