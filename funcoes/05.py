'''5. Crie uma função chamada contar_vogais que recebe uma string como parâmetro. Implemente a lógica para contar o número de vogais na string e retorne o total de vogais. Solicite ao usuário para inserir uma frase e utilize a função para contar as vogais.'''

# Definição da função contar_vogais
def contar_vogais(frase):
    vogais = "aeiouAEIOU"
    return sum(1 for char in frase if char in vogais)

# Leitura da frase e chamada da função
frase_usuario = input("Digite uma frase: ")
total_vogais = contar_vogais(frase_usuario)
print(f"Total de vogais na frase: {total_vogais}")
