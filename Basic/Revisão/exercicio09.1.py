decisao = "s"

while decisao == "s" or decisao == "S":
    num = int(input("Digite um número: "))

    antecessor = num - 1

    print(f"O número antecessor de {num} é {antecessor}.")
    decisao = input("Deseja continuar? (s/n) \n")
else:
    print("Programa encerrado.")