decisao = "s"

while decisao == "s" or decisao == "S":
    macas = int(input("Quantas maçãs deseja comprar? "))

    if macas < 12:
        valor = macas * 1.3
        print(f"Ao comprar {macas} maçãs, você paga R${valor}.")
    else:
        valor = macas * 1.0
        print(f"Ao comprar {macas} maçãs, você paga R${valor}.")
    decisao = input("Deseja continuar? (s/n) \n")
else:
    print("Programa encerrado.")