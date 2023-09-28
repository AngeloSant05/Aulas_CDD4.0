decisao = "s"

while decisao == "s" or decisao == "S":
    base = float(input("Digite o valor da base: "))
    while base <= 0:
        base = float(input("Valor inválido. Digite o valor novamente: "))
    else:
        altura = float(input("Digite o valor da altura: "))
        while altura <= 0:
            altura = float(input("Valor inválido. Digite o valor novamente: "))
        else:
            area = (base * altura) / 2
            print(f"{area}")
            decisao = input("Deseja continuar? (s/n) \n")
else:
    print("Programa encerrado.")
