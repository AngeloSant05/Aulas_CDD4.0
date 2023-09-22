numero = int(input("Digite um número: "))
for x in range(numero+1):
    for y in range(1, x+1):
        print(f"{y}", end=" ")
    print()
