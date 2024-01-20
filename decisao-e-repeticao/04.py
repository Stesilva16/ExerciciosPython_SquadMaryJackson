'''4. Implemente um programa que classifique um aluno com base em sua pontuação em um exame. O programa deverá solicitar uma nota de 0 a 10. Se a pontuação for maior ou igual a 7, o aluno é aprovado; caso contrário, é reprovado.'''

# Solicitação da nota ao usuário
nota = float(input("Digite a nota do aluno (de 0 a 10): "))

# Verificação e impressão da classificação
if nota >= 7:
    print("Aluno aprovado!")
else:
    print("Aluno reprovado.")
