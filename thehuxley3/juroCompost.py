valor_inicial = float(input())
taxa_juros = float(input())
periodo = int(input())



def valor_final(valorInicial, taxaJuros, periodo):
    valor_final = valorInicial
    for ano in range(periodo):
        valor_final = valor_final * (1 + taxaJuros)
    valor_final = round(valor_final, 2)
    return valor_final
    
#//TODO: Iterar, baseado no período em anos, para calculo do valorFinal com os juros.

print("Valor final do investimento: R$", valor_final(valor_inicial, taxa_juros, periodo))