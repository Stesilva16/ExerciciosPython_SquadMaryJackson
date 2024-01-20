'''9. O programa deve calcular e apresentar a quantidade de números pares e ímpares inseridos. O processo de leitura deve ser encerrado quando o usuário informar o valor zero. Certifique-se de incluir validações para garantir que apenas números positivos sejam considerados na contagem e cálculos.'''

# Inicialização das variáveis de contagem
pares = 0
impares = 0

# Loop para leitura e contagem
while True:
    numero = int(input("Digite um número (ou 0 para encerrar): "))
    
    if numero == 0:
        break
    
    if numero > 0:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1

# Impressão dos resultados
print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")
