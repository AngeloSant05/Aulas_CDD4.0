qtd = int(input("Quantos alunos temos na sala? "))
nomes = []

for x in range(qtd):
    nomes.append(input("Digite o nome do aluno: "))
for i in range(qtd):
    print(f"O aluno {nomes[i]} está na posição {i} e no rank {i+1}.")
