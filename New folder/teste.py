with open("nova_senha.txt", "w") as arquivo:
    arquivo.write("Essa é a minha nova senha\n")

with open("nova_senha.txt", "a") as arquivo:
    arquivo.write("123456")

with open("nova_senha.txt", "r") as arquivo:
    print(arquivo.read())
