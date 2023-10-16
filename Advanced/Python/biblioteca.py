import random


def imprime_nome(nome):
    print(f"Nome: {nome}")


def somar(num1, num2):
    resp = num1 + num2
    print(f"\nO resultado da soma foi {resp}")


def subtrair(num1, num2):
    resp = num1 - num2
    print(f"\nO resultado da subtração foi {resp}")


def dividir(num1, num2):
    resp = num1 / num2
    print(f"\nO resultado da divisão foi {resp}")


def multiplicar(num1, num2):
    resp = num1 * num2
    print(f"\nO resultado da multiplicação foi {resp}")


def repete_num(num):
    for x in range(1, num+1):
        print(x * str(x), end=" ")
        print("\n")


def escadinha(num):
    for x in range(1, num+1):
        for y in range(1, x+1):
            print(y, end=" ")
        print("\n")


def contagem_vogal(texto):
    vogal = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    contador = 0
    for x in texto:
        if x in vogal:
            contador += 1
    print(f"O texto possui {contador} vogais")


def estoque(produto, qtd, valor):
    valor_estoque = qtd * valor
    return valor_estoque


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()