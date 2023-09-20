num = float(input("Insira um valor: "))
num1 = float(input("Insira outro valor: "))

while num1 == 0:
    num1 = float(input("Valor inválido. \nInsira outro valor: "))
div = num / num1
print(div)
