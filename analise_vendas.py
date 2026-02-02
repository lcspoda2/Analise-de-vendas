vendas = {
    'camisa': 130,
    'tenis': 600,
    'calca': 300,
    'bone': 60
}


def analisar_vendas(dados):
    vendas_altas = {}
    vendas_baixas = {}

    total_altas = 0
    total_baixas = 0

    for produto, valor in dados.items():
        if valor >= 200:
            vendas_altas[produto] = valor
            total_altas += valor
        else:
            vendas_baixas[produto] = valor
            total_baixas += valor

    return vendas_altas, vendas_baixas, total_altas, total_baixas


altas, baixas, total_altas, total_baixas = analisar_vendas(vendas)

print("Produtos com vendas altas:")
print(altas)
print("Total vendas altas:", total_altas)

print("\nProdutos com vendas baixas:")
print(baixas)
print("Total vendas baixas:", total_baixas)
