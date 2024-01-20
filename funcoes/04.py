'''4. Crie um programa que leia quanto dinheiro uma pessoa tem na carteira, e calcule quanto poderia comprar de cada moeda estrangeira. 
Considere a tabela de conversão abaixo: 
Dólar Americano: R$ 4,91 
Peso Argentino: R$ 0,02 
Dólar Australiano: R$ 3,18 
Dólar Canadense: R$ 3,64 
Franco Suiço: R$ 0,42 
Euro: R$ 5,36 
Libra esterlina: R$ 6,21'''

# Definição da função de conversão
def converter_moeda(valor, taxa):
    return valor * taxa

# Tabela de conversão
tabela_conversao = {
    "Dólar Americano": 4.91,
    "Peso Argentino": 0.02,
    "Dólar Australiano": 3.18,
    "Dólar Canadense": 3.64,
    "Franco Suiço": 0.42,
    "Euro": 5.36,
    "Libra esterlina": 6.21
}

# Leitura do valor em reais
reais = float(input("Digite a quantia em reais: "))

# Conversão e impressão dos resultados
for moeda, taxa in tabela_conversao.items():
    valor_convertido = converter_moeda(reais, taxa)
    print(f"Com R${reais:.2f} você pode comprar {valor_convertido:.2f} {moeda}")