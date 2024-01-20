'''10. Faça um programa que lê três números inteiros e os mostra em ordem crescente.'''

# Solicitação de três números ao usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Ordenação e impressão dos números em ordem crescente
numeros_ordenados = sorted([num1, num2, num3])
print(f"Números em ordem crescente: {numeros_ordenados}")
