'''3. Faça um Programa que peça a quantidade de quilômetros, transforme em metros, centímetros e milímetros.'''

#Pergunta ao usuário
quilometros = float(input("Digite a quantidade de quilômetros: "))

# Conversões
metros = quilometros * 1000
centimetros = quilometros * 100000
milimetros = quilometros * 1000000

# Impressão dos resultados
print(f"{quilometros} quilômetros são equivalentes a:")
print(f"{metros} metros")
print(f"{centimetros} centímetros")
print(f"{milimetros} milímetros")