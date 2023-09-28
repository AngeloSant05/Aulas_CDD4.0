while True:
    num = int(input("Digite um número: "))
    menu = input("Digite\n(1 para o antecessor | 2 para o sucessor | 3 para encerrar.)\n")
    while menu != "1" and menu != "2" and menu != "3":
        menu = input("Valor inválido.\nDigite\n(1 para o antecessor | 2 para o sucessor | 3 para encerrar)\n")

    antecessor = num - 1
    sucessor = num + 1

    if menu == "1":
        print(f"O número antecessor de {num} é {antecessor}.")
    elif menu == "2":
        print(f"O número sucessor de {num} é {sucessor}.")
    else:
        break
print("Programa encerrado.")
