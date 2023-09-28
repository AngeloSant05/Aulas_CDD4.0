decisao = "s"

while decisao == "s" or decisao == "S":
    valor1 = float(input("Digte o primeiro valor: "))
    valor2 = float(input("Digte o segundo valor: "))

    if valor1 > valor2:
        print(f"{valor2}, {valor1}")
    else:
        print(f"{valor1}, {valor2}")
    decisao = input("Deseja continuar? (s/n) \n")
else:
    print("Programa encerrado.")