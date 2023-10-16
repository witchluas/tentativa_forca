# Lista de palavras para o jogo
import random

palavras = ["python", "computador", "programador", "analista"]

# Escolha uma palavra aleatória
palavra = random.choices(palavras)

# Inicialização das variáveis
tentativas = 6
letras_certas = []
letras_erradas = []

while True:
    print("------ Jogo da Forca -----")
    print(f"Tentativas restantes: {tentativas}")

    # Exiba as letras adivinhadas até agora
    palavra_mostrada = ''
    for letra in palavra:
        if letra in letras_certas:

        else:
              palavra_mostrada += '_'

    # Exiba as letras erradas
    print("Letras erradas: " + ' '.join(letras_erradas))

    if palavra_mostrada == palavra:
        print("Parabéns! Você venceu!")
        break

    if tentativas == 0:
        print(f"Fim de jogo! A palavra era '{palavra}'.")
        break

    # Peça ao jogador para adivinhar uma letra
    letra = input("Digite uma letra: ").lower()

    if letra in letras_certas or letra in letras_erradas:
        print("Você já tentou esta letra.")
    elif letra in palavra:
        letras_certas.append(letra)
    else:
        letras_erradas.append(letra)
        tentativas -= 1

