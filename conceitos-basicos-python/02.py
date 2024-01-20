'''2. Peça ao usuário para informar o ano de nascimento. Em seguida,
calcule e imprima a idade atual.'''

#Pergunta ao usuário
ano_nascimento = int(input("Digite o ano de nascimento: "))

# Calculando a idade atual
ano_atual = 2024  # Ano atual (pode variar dependendo do ano em que você está)
idade_atual = ano_atual - ano_nascimento

# Impressão do resultado
print(f"Sua idade atual é: {idade_atual} anos")
