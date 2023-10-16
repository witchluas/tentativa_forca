from biblioteca import*
random
palavras = []
letras_usuario = []
tentavita_letra = []
chances = 7
ganhou = False

while True:
    if letra in palavras:
        if letra.lower() in letras_usuario:
            print(letra, end=" ")
        else:
            print("_", end=" ")
    print(f"Você tem {chances} chances")
    tentativa_letra= input("Escolha uma letra para adivinhar: ").lower()
    letras_usuario.append(tentativa_letra.lower())
    if tentativa_letra.lower() not in palavras.lower():
        chances -= 1

        ganhou = True
        for letra in palavras:
            if letra.lower() not in letras_usuario:
                ganhou = False


        if chances == 0 or ganhou:
            break



if ganhou:
     print(f"Parabéns, você ganhou. A palavra era: {palavras}")

else:
    print(f"Infelizmente você perdeu! A palavra era: {palavras}")

