decisao = "s"

while decisao == "s" or decisao == "S":
    base = float(input("Digite o valor da base: "))
    altura = float(input("Digite o valor da altura: "))

    area = (base * altura) / 2

    print(f"{area}")
    decisao = input("Deseja continuar? (s/n) \n")
else:
    print("Programa encerrado.")
