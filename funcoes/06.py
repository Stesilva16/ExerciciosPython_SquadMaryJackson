'''6. Vamos construir um jogo de forca. O programa escolherá aleatoriamente uma palavra secreta de uma lista predefinida. A palavra secreta será representada por espaços em branco, um para cada letra da palavra. O jogador terá um número limitado de 6 tentativas. Em cada tentativa, o ogador pode fornecer uma letra. Se a letra estiver presente na palavra secreta, ela será revelada nas posições correspondentes. Se a letra não estiver na palavra, uma mensagem de erro deverá ser informada. Após um número máximo de erros, o jogador perde. O jogo continua até que o jogador adivinhe a palavra ou exceda o número máximo de tentativas. 
Dica: Você precisará importar uma biblioteca para resolver esse exercício'''

# Importação da biblioteca necessária
import random

# Lista de palavras predefinidas
palavras_secretas = ["python", "programacao", "desenvolvimento", "computador", "tecnologia"]

# Escolha aleatória de uma palavra
palavra_secreta = random.choice(palavras_secretas)

# Inicialização de variáveis
tentativas_maximas = 6
tentativas = 0
letras_reveladas = ['_'] * len(palavra_secreta)

# Função para exibir o status do jogo
def exibir_status():
    print("Palavra secreta: " + " ".join(letras_reveladas))
    print("Tentativas restantes: " + str(tentativas_maximas - tentativas))

# Loop principal do jogo
while "_" in letras_reveladas and tentativas < tentativas_maximas:
    exibir_status()
    letra = input("Digite uma letra: ").lower()
    
    if letra.isalpha() and len(letra) == 1:
        if letra in palavra_secreta:
            for i, char in enumerate(palavra_secreta):
                if char == letra:
                    letras_reveladas[i] = letra
            print("Letra correta!")
        else:
            tentativas += 1
            print("Letra incorreta. Tente novamente.")
    else:
        print("Entrada inválida. Digite uma única letra.")

# Exibição do resultado final
exibir_status()
if "_" not in letras_reveladas:
    print("Parabéns! Você adivinhou a palavra.")
else:
    print(f"Você excedeu o número máximo de tentativas. A palavra era: {palavra_secreta}")