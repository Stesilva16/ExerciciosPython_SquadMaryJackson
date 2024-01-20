'''6. Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas. Dica: lembre−se que ao informar o nome o usuário pode igitar letras maiúsculas ou minúsculas'''

# Entrada do nome do usuário
nome_usuario = input("Digite seu nome: ")

# Inversão do nome e conversão para maiúsculas
nome_invertido = nome_usuario[::-1].upper()

# Impressão do resultado
print(f"Seu nome ao contrário: {nome_invertido}")