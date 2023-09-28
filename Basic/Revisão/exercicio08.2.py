quantidade = int(input("Digite quantos números deseja adicionar: "))
soma = 0

for x in range(quantidade):
    num = float(input("Digite um número: "))
    soma += num
media = soma / quantidade
print(f"Valor da soma é: {soma}")
print(f"{media}")
