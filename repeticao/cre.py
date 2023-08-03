matricula = input()
cre = float(input())
contador_cre = cre
contador_quantidade = 1

while True:
    cre_aux = cre
     
    matricula_ = input()
    if matricula_ == '999':
        break
    cre_ = float(input())

    contador_cre += cre_
    contador_quantidade +=1
    matricula_aux = matricula
    if cre_ < cre_aux :
        cre_aux = cre_
        matricula_aux = matricula_

print(matricula_aux)
print(f"{contador_cre / contador_quantidade:.2f}")