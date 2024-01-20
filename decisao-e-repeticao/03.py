'''3. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.'''

# Loop para entrada da nota válida
while True:
    nota = float(input("Digite uma nota entre zero e dez: "))
    if 0 <= nota <= 10:
        break
    else:
        print("Nota inválida. Tente novamente.")

print(f"Você digitou a nota: {nota}")