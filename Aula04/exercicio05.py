contador = 0

for x in range(0, 10):
    num = int(input("Digite um número: "))
    if num < 0:
        contador += 1
        print(f"{num} é um número negativo.")
if contador == 0:
    print(f"Não ouve números negativos")
else:
    if contador == 1:
        print(f"Tivemos um total de {contador} número negativo")
    else:
        print(f"Tivemos um total de {contador} números negativos")
