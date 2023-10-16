import random

def jogo_da_forca():
    palavras = []

    def escolher_palavra ():
        palavras= list [("praia"),
        ("cinema"),
        ("python"),
        ("sephora"),
        ("bolo"),
        ("brownie"),
        ("livros"),
        ("baunilha"),
        ("cappucino"),
        ("café")]

    palavra = random.choice(palavras)
    return palavra

#boneco
def boneco (erros):
    partes_boneco = [" O", "/|\\", "\\"]
    print("\n >>>>>>>>>>>>>>> FORCA <<<<<<<<<<<<<< ")
    for i in range (erros):
        if i < len(partes_boneco):
            print(partes_boneco [i])

def forca ():
    print(" SEJAM BEM-VINDOS AO JOGO DA FORCA ")

    palavras = []
    letras_usuario = []
    chances = 7
    ganhou = False