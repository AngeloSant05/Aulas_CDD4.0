decisao = "s"

while decisao == "s" or decisao == "S":
    num = int(input("Digite um número: "))

    sucessor = num + 1

    print(f"O número sucessor de {num} é {sucessor}.")
    decisao = input("Deseja continuar? (s/n) \n")
else:
    print("Programa encerrado.")