import json

# Simulação de JSON de faturamento diário
faturamento_diario = """
{
    "dias": [
        {"dia": 1, "faturamento": 2000.0},
        {"dia": 2, "faturamento": 3000.0},
        {"dia": 3, "faturamento": 0.0},
        {"dia": 4, "faturamento": 4500.0},
        {"dia": 5, "faturamento": 500.0},
        {"dia": 6, "faturamento": 0.0}
    ]
}
"""

# Carregando dados do JSON
dados = json.loads(faturamento_diario)["dias"]

def calcular_faturamento(dados):
    # Filtrando os dias com faturamento (ignorando finais de semana e feriados)
    dias_com_faturamento = [d["faturamento"] for d in dados if d["faturamento"] > 0]

    # Calculando o menor, maior e a média do faturamento
    menor_faturamento = min(dias_com_faturamento)
    maior_faturamento = max(dias_com_faturamento)
    media_faturamento = sum(dias_com_faturamento) / len(dias_com_faturamento)

    # Contando os dias com faturamento acima da média
    dias_acima_da_media = sum(1 for faturamento in dias_com_faturamento if faturamento > media_faturamento)

    return menor_faturamento, maior_faturamento, dias_acima_da_media

menor, maior, acima_media = calcular_faturamento(dados)

print(f"Menor faturamento: R${menor:.2f}")
print(f"Maior faturamento: R${maior:.2f}")
print(f"Dias com faturamento acima da média: {acima_media}")
