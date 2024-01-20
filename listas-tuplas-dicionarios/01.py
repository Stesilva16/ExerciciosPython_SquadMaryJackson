'''1. Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
""Telefonou para a vítima?"" 
""Esteve no local do crime?"" 
""Mora perto da vítima?"" 
""Devia para a vítima?"" 
""Já trabalhou com a vítima?"" 
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como ""Suspeita"", entre 3 e 4 como ""Cúmplice"" e 5 como ""Assassino"". Caso contrário, ele será classificado como""Inocente"".'''

# Inicialização da lista de perguntas
perguntas = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?"
]

# Inicialização da contagem de respostas positivas
respostas_positivas = 0

# Pergunta ao usuário e contagem de respostas positivas
for pergunta in perguntas:
    resposta = input(pergunta + " (Sim/Não): ")
    if resposta.lower() == "sim":
        respostas_positivas += 1

# Classificação da participação no crime
if respostas_positivas == 2:
    print("Suspeita")
elif 3 <= respostas_positivas <= 4:
    print("Cúmplice")
elif respostas_positivas == 5:
    print("Assassino")
else:
    print("Inocente")