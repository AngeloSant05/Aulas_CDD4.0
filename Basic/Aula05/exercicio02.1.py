cont = 1
soma = 0
quant = int(input("Digite a quantidade de vezes que quer repetir: "))

while cont <= quant:
    num = float(input("Digite sua nota: "))
    soma += num
    cont += 1
print(f"{soma / quant}")

# Outra forma de calcular

# media = soma / quant
# print(media)