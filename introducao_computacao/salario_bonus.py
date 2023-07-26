nome = input()
salario_fixo = float(input())
total_vendas = float(input())


def bonificacao(salario_fixo, total_vendas):
    bonus = salario_fixo + (total_vendas * 0.15)
    return bonus


salario_final = (bonificacao(salario_fixo, total_vendas))

print(f"TOTAL = R$ {salario_final:.2f}")
