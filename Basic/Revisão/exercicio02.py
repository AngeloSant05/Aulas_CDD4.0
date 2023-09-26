decisao = "s"

while decisao == "s" or decisao == "S":
    num = float(input("Digite um valor: "))

    while num == 0:
        num = float(input("Número inválido.\nDigite outro valor: "))
    if num > 0:
        print(f"O número {num} é positivo.")
    else:
        print(f"O número {num} é negativo.")
    decisao = input("Deseja continuar? (s/n) \n")
else:
    print("Progrma encerrado.")
