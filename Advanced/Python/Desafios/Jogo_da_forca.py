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



