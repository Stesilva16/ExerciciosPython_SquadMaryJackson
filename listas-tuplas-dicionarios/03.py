'''3. Crie um dicionário representando um carrinho de compras. Adicione produtos (chaves) e quantidades (valores) ao carrinho. Calcule o total do carrinho de compra.'''

# Inicialização do dicionário representando o carrinho de compras
carrinho_compras = {"produto1": 10, "produto2": 5, "produto3": 3}

# Cálculo do total do carrinho de compras
total_carrinho = sum(valor for valor in carrinho_compras.values())

# Impressão do resultado
print(f"Total do carrinho de compras: R${total_carrinho:.2f}")