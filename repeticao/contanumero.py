numero = int(input())
contador = 0
contador_numero = 0
contador_quantidade = 0

for i in range(20):
    numero_ = int(input())
    
    
    if (numero_ > 0) and (numero_ < 15 or numero_ > 20):
        contador_numero += numero_
        contador_quantidade += 1

    if numero_ == numero:
        contador += 1
    
    if numero_ == -1:
        break

if contador >=0 :
    print(f"O número {numero} apareceu {contador} vez(es)")
if contador_quantidade > 0:
    print(f"A média dos números foi de: {contador_numero/contador_quantidade:.2f}")
else:
    print("Sem valores para calcular a média")
