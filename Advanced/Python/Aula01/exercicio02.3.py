from Advanced.Python.biblioteca import *

decisao = "s"

while decisao == "s" or decisao == "S":
    print("=======================================")
    print("Para somar dois números digite(1)")
    print("Para subbtrair dois números digite(2)")
    print("Para multiplicar dois números digite(3)")
    print("Para dividir dois números digite(4)")
    print("=======================================")
    resposta = input("\nEscolha: ")

    while resposta != "1" and resposta != "2" and resposta != "3" and resposta != "4":
        resposta = input("Valor inválido. Digite novamente: ")
    else:
        num1 = float(input("\nDigite o primeiro valor: "))
        num2 = float(input("\nDigite o segundo valor: "))

        if resposta == "1":
            somar2(num1, num2)
        elif resposta == "2":
            subtrair2(num1, num2)
        elif resposta == "3":
            multiplicar2(num1, num2)
        elif resposta == "4":
            dividir2(num1, num2)

        decisao = input("\nDeseja repetir? [S/N] ")
        print(end="\n")
else:
    print("Programa encerrado")
