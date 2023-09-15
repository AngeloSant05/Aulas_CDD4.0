contador = 0
soma_nega= 0

for x in range(0, 10):
    num = int(input("Digite um número: "))
    if num < 0:
        contador += 1
        print(f"{num} é um número negativo.")
        soma_nega += num
if contador == 0:
    print(f"Não ouve números negativos")
else:
    if contador == 1:
        print(f"Tivemos um total de {contador} número negativo")
        print(f"E esse foi o número: {soma_nega}")
    else:
        print(f"Tivemos um total de {contador} números negativos")
        print(f"E essa foi a soma dos números negativos: {soma_nega}")

