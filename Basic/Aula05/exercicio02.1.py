cont = 1
soma = 0
qtd = int(input("Informe a quantidade de notas: "))

while cont <= qtd:
    num = float(input("Digite sua nota: "))
    soma += num
    cont += 1
print(f"{soma / qtd}")

# Outra forma de calcular

# media = soma / quant
# print(media)