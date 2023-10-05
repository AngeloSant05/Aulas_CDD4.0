from Advanced.Python.biblioteca import *

decisao = "s"

while decisao == "s" or decisao == "S":
    print("=======================================")
    print("Para somar dois números digite(1)")
    print("Para subbtrair dois números digite(2)")
    print("Para multiplicar dois números digite(3)")
    print("Para dividir dois números digite(4)")
    print("=======================================")
    resposta = int(input("\nEscolha: "))

    num1 = float(input("\nDigite o primeiro valor: "))
    num2 = float(input("\nDigite o segundo valor: "))

    if resposta == 1:
        somar(num1, num2)
    elif resposta == 2:
        subtrair(num1, num2)
    elif resposta == 3:
        multiplicar(num1, num2)
    elif resposta == 4:
        dividir(num1, num2)
    else:
        print("\nValor inválido")

    decisao = input("\nDeseja repetir? [S/N] ")
else:
    print("\nPrograma encerrado")