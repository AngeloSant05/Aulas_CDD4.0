cont = 1
soma = 0
qtd = int(input("Informe a quantidade de notas: "))

while cont <= qtd:
    num = float(input("Digite sua nota: "))
    soma += num
    cont += 1
media = soma / qtd
print(media)
