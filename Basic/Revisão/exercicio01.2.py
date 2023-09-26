decisao = "s"

while decisao == "s" or decisao == "S":
    num1 = float(input("Digite um número: "))
    num2 = float(input("Digite outro número: "))

    media = (num1 + num2) / 2

    if media >= 7:
        print(f"Parabéns você foi aprovado, sua nota foi: {media}")
    elif media >= 4:
        print(f"Você está de recuperação se empenhe mais, sua nota foi: {media}")
    else:
        print(f"Você foi reprovado, vá tirar foto com o professor."
              f"\n              Sua nota foi: {media}")

    decisao = input("Deseja continuar? (s/n)\n")
else:
    print(f"Programa encerrado.")
