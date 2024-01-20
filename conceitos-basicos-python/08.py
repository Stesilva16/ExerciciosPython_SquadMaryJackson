'''Faça um Programa que pergunte quanto você ganha por hora e o
número de horas trabalhadas no mês.Calcule e mostre o total do seu
salário no referido mês.'''

#Pergunta ao usuário
ganho_por_hora = float(input("Digite quanto você ganha por hora: "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))

# Cálculo do salário mensal
salario_mensal = ganho_por_hora * horas_trabalhadas

# Impressão do resultado
print(f"Seu salário mensal é: R${salario_mensal:.2f}")