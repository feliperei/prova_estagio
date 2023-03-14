# Dicionário com o valor de faturamento mensal por estado
faturamento = {'SP': 67836.43, 'RJ': 36678.66, 'MG': 29229.88, 'ES': 27165.48, 'Outros': 19849.53}

# Cálculo do valor total mensal
total_mensal = sum(faturamento.values())

# Cálculo do percentual de representação de cada estado no valor total mensal
percentuais = {estado: (valor / total_mensal) * 100 for estado, valor in faturamento.items()}

# Exibição dos resultados
for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")
