# Variáveis
num1 = int(input("Diga-me um número: "))
num2 = int(input("Diga-me outro número: "))

print(f"Os seus números são: {num1}, {num2}")

if num1 == num2:
    print("Os números são iguais.")
else:
    if num1 > num2:
        print(f"Essa é a ordem crescente entre eles: {num2}, {num1}")
    else:
        print(f"Essa é a ordem crescente entre eles: {num1}, {num2}")
