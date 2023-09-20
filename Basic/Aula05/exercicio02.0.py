cont = 1
soma = 0

while cont <= 10:
    num = float(input("Digite sua nota: "))
    soma += num
    cont += 1
media = soma / 10
print(media)
