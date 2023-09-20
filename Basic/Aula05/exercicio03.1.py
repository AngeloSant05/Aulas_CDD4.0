num = float(input("Insira um valor: "))
num1 = float(input("Insira outro valor: "))
cont = 1

while num1 == 0:
    num1 = float(input("Valor inválido.\nInsira outro valor: "))
    cont += 1
    if cont >= 5:
        print("Número de tentativas alcançadas.")
        break
else:
    div = num / num1
    print(div)
