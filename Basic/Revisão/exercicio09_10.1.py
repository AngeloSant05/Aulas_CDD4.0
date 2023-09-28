num = int(input("Digite um número: "))

menu = int(input("Digite 1 para o antecessor, 2 para o sucessor e 3 para encerrar o código: "))
while menu != 1 and menu != 2 and menu != 3:
    menu = int(input("Valor inválido.\nDigite 1 para o antecessor, 2 para o sucessor e 3 para encerrar o código: "))

antecessor = num - 1
sucessor = num + 1

if menu == 1:
    print(f"O número antecessor de {num} é {antecessor}.")
elif menu == 2:
    print(f"O número sucessor de {num} é {sucessor}.")
else:
    print(f"Programa encerrado.")
