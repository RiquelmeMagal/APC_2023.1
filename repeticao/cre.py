matricula = input()
cre = float(input())

aux_matricula = ''
cont = 0
cres = 0
while True:

    aux_matricula = input()
    if aux_matricula == '999':
        break
    aux_cre = float(input())
    cont += 1
    cres += aux_cre
    if aux_matricula > matricula:
        matricula = aux_matricula
        cre = aux_cre

media_ = cres / cont
print(matricula)
print(f"{media_:.2f}")
