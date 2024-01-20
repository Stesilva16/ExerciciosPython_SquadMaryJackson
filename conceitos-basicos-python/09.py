'''Solicite ao usuário o número de horas de exercício físico por semana.
Calcule o total de calorias queimadas em um mês, considerando uma
média de 5 calorias por minuto de exercício.'''

#Pergunta ao usuário
horas_exercicio_semana = float(input("Digite o número de horas de exercício físico por semana: "))

# Cálculo do total de calorias queimadas em um mês
calorias_por_minuto = 5
calorias_queimadas_por_semana = horas_exercicio_semana * 60 * calorias_por_minuto
calorias_queimadas_por_mes = calorias_queimadas_por_semana * 4  # Supondo um mês com 4 semanas

# Impressão do resultado
print(f"Você queimou um total de {calorias_queimadas_por_mes} calorias neste mês.")