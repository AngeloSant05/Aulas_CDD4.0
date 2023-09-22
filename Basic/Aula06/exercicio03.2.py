numero = int(input("Digite um número: "))
contador = 0

while contador < numero + 1:
    y = 1
    while y < contador + 1:
        print(y, end=" ")
        y += 1
    print()
    contador += 1
