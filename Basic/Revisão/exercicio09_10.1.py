num = int(input("Digite um número: "))

menu = int(input("Digite\n(1 para o antecessor | 2 para o sucessor)\n"))
while menu != 1 and menu != 2:
    menu = input("Valor inválido.\nDigite\n(1 para o antecessor | 2 para o sucessor)\n")

antecessor = num - 1
sucessor = num + 1

if menu == 1:
    print(f"O número antecessor de {num} é {antecessor}.")
else:
    print(f"O número sucessor de {num} é {sucessor}.")
