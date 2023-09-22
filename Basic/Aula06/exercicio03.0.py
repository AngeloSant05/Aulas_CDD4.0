numero = int(input("Digite um número: "))
contador = 0

while contador != numero+1:
    print(f"{contador*str(contador)}", end="\n")
    contador += 1
