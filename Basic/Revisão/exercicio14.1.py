decisao = "s"

while decisao == "s" or decisao == "S":
    temperatura = float(input("Digite a sua temperatura em Fahrenheit: "))

    C = ((temperatura - 32) / 9) * 5

    print(f"O valor de {temperatura}F vale em Celsius {C}ºC")
    decisao = input("Deseja continuar? (s/n) \n")
else:
    print("Programa encerrado.")
