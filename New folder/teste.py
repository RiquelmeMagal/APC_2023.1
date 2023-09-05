with open("nova_senha.txt", "w") as arquivo:
    arquivo.write("Essa é a minha nova senha\n")

with open("nova_senha.txt", "a") as arquivo:
    arquivo.write("123456")

with open("nova_senha.txt", "r") as arquivo:
    print(arquivo.read())

def ler_arquivo():
    try:
        with open("nova_senha.txt", "r") as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                print(linha.strip())
    except FileNotFoundError:
        print("O arquivo 'nova_senha.txt' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {str(e)}")

ler_arquivo()
