from Advanced.Python.biblioteca import estoque

produto = input("Digite o nome do produto: ")
qtd = int(input("Quantos produtos temos no estoque? "))
valor = float(input("Qual o valor do produto? "))

tv = estoque(qtd, valor)

print(tv)
