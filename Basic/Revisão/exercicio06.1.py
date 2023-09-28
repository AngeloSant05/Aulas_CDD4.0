decisao = "s"

while decisao == "s" or decisao == "S":
    num = float(input("Digite um número: "))

    if num == 10:
        print(f"É IGUAL A 10!")
    elif num > 10:
        print(f"É MAIOR QUE 10!")
    else:
        print(f"NÃO É MAIOR QUE 10!")
    decisao = input("Deseja continuar? (s/n) \n")
else:
    print(f"Programa encerrado.")