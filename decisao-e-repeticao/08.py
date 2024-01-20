'''8. Criar um programa em Python que solicite três números ao usuário, utilize estruturas condicionais para determinar o maior entre eles e apresente o resultado.'''

# Solicitação de três números ao usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Verificação e impressão do maior número
maior_numero = max(num1, num2, num3)
print(f"O maior número é: {maior_numero}")
