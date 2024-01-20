'''3. Escreva um script que pergunta ao usuário se ele deseja converter uma temperatura de grau Celsius para Fahrenheit ou vice-versa. Para cada opção, crie uma função. 
Plus: Crie uma terceira, que é um menu para o usuário escolher a opção desejada, onde esse menu chama a função de conversão correta.'''

# Definição das funções de conversão
def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Função de menu
def menu_conversao():
    print("Escolha a opção:")
    print("1. Celsius para Fahrenheit")
    print("2. Fahrenheit para Celsius")
    opcao = int(input())
    
    if opcao == 1:
        celsius = float(input("Digite a temperatura em graus Celsius: "))
        print(f"A temperatura em Fahrenheit é: {celsius_para_fahrenheit(celsius)}")
    elif opcao == 2:
        fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))
        print(f"A temperatura em Celsius é: {fahrenheit_para_celsius(fahrenheit)}")
    else:
        print("Opção inválida")

# Exemplo de uso do menu
menu_conversao()