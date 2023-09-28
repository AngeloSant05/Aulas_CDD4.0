decisao = "s"

while decisao == "s" or decisao == "S":
    num = int(input("Digite um número: "))

    if num % 2 == 0:
        print(f"O número {num} é par.")
    else:
        print(f"O número {num} é ímpar.")
    decisao = input("Deseja continuar? (s/n) \n")
else:
    print("Programa encerrado")
