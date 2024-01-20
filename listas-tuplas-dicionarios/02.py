'''2. Faça um Programa que peça as quatro notas de 5 alunos, calcule e armazene numa lista a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0. '''

# Inicialização da lista de médias
medias_alunos = []

# Loop para entrada das notas e cálculo da média
for i in range(5):
    notas = [float(input(f"Informe a nota {j+1} do aluno {i+1}: ")) for j in range(4)]
    media = sum(notas) / len(notas)
    medias_alunos.append(media)

# Contagem de alunos com média maior ou igual a 7.0
alunos_aprovados = sum(media >= 7.0 for media in medias_alunos)

# Impressão do resultado
print(f"Número de alunos com média maior ou igual a 7.0: {alunos_aprovados}")