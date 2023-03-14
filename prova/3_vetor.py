import json

# Leitura dos dados do arquivo JSON
with open('faturamento.json') as file:
    data = json.load(file)

# Cálculo do menor e maior valor de faturamento diário
min_faturamento = min(data.values())
max_faturamento = max(data.values())

# Cálculo da média mensal de faturamento diário
faturamento_total = sum(data.values())
dias_mes = len(data)
media_mensal = faturamento_total / dias_mes

# Cálculo do número de dias em que o faturamento diário foi superior à média mensal
dias_acima_media = sum(1 for faturamento in data.values() if faturamento > media_mensal)

# Exibição dos resultados
print("Menor valor de faturamento diário:", min_faturamento)
print("Maior valor de faturamento diário:", max_faturamento)
print("Número de dias com faturamento acima da média mensal:", dias_acima_media)
