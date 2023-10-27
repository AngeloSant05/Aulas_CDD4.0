from Advanced.Python.biblioteca import *

palavra1 = ["a", "b", "a", "c", "a", "t", "e"]
palavra2 = ["d", "o", "z", "e"]
palavra3 = ["t", "r", "e", "v", "a", "s"]
palavra4 = ["l", "u", "z"]
palavra5 = ["j", "a", "m", "b", "a", "l", "a", "i", "a"]
contador = 0
palavra_escolhida = 1
entrada = input("Digite uma letra: ")
resposta = []

if palavra_escolhida == 1:
    print("_ _ _ _ _ _ _")
    while contador < 6:
        for x in entrada:
            if x in palavra1:

            else:
                contador += 1

from Advanced.Python.biblioteca import *

usuario = []
erros = 0
venceu = False
palavras = ["abacate", "ovo", "cuscuz", "batata"]
escolhida = random.choice(palavras)
print("---Bem-vindo ao jogo da forca.---")
while True:
    escolha = input("Digite uma letra: ")
    usuario.append(escolha.lower)
    for letra in escolhida:
        if letra.lower() in usuario:
            print(letra, end=" ")
        else:
            print("_", end=" ")
    print()

    if escolha.lower() not in escolhida.lower():
        erros += 1
        print(f"Você tem {7 - erros} tentativas.")
        desenha_forca(erros)

    venceu = True
    for letra in escolhida:
        if letra.lower() not in usuario:
            venceu = False

    if erros == 7 or venceu:
        break



