pregos_disponiveis = 12
preco_caixa = 7.89
total_pregos_necessarios = 0
preco_caixas = 0

lista = []

while True:
    numero = int(input())
    lista.append(numero)
    if numero % 2 != 0:
        total_gasto = preco_caixas + (total_pregos_necessarios // 12) * preco_caixa
        # Verificação para caso meia caixa resolva o problema
        if total_gasto < preco_caixa:
            total_gasto = preco_caixa
        print(f"{total_gasto:.2f}")
        break
    
    total_pregos_necessarios += numero
    if pregos_disponiveis < numero:
        caixas_compradas = (numero - pregos_disponiveis + 11) // 12
        pregos_disponiveis += caixas_compradas * 12
        preco_caixas = caixas_compradas * preco_caixa

    pregos_disponiveis -= numero

print(pregos_disponiveis)
