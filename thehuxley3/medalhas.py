dicionario = {}

while True:
    pais_medalha = input().replace(' ','').replace(',', ' ').split()
    if pais_medalha[0] == "*":
        break
    else:
        if pais_medalha[0] not in dicionario:
            dicionario[pais_medalha[0]] = [pais_medalha[1]] 
        else:
            dicionario[pais_medalha[0]].append(pais_medalha[1])

print(dicionario)

