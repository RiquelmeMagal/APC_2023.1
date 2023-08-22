def verifica_permutacao(palavra_a, palavra_b):
    return sorted(palavra_a) == sorted(palavra_b)


exemplo1 = verifica_permutacao("amor", "roma")
exemplo2 = verifica_permutacao("metro", "morte")
exemplo3 = verifica_permutacao("amor", "amora")
exemplo4 = verifica_permutacao("anda", "nada")

print(exemplo1)  
print(exemplo2)  
print(exemplo3)
print(exemplo4)
