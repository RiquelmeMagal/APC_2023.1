palavra = "bct"

nova_palavra = ''

for i in range(len(palavra),0,-1):
    nova_palavra += palavra[i-1]

print(nova_palavra)
