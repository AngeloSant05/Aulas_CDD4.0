from Advanced.Python.biblioteca import estoque

produto = input("Digite o nome do produto: ")
qtd = int(input("Quantos produtos temos no estoque? "))
valor_und = float(input("Qual o valor do produto? "))

estoque(produto, qtd, valor_und)