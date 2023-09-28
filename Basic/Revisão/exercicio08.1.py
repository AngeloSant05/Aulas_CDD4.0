decisao = "s"

while decisao == "s" or decisao == "S":
    soma = 0

    for x in range(4):
        num = float(input("Digite um número: "))
        soma += num
    media = soma / 4
    print(f"Valor da soma é: {soma}")
    print(f"{media}")
    decisao = input("Deseja continuar? (s/n) \n")
else:
    print("Programa encerrado.")
