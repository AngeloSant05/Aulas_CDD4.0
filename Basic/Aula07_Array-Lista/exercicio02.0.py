qtd = int(input("Quantos alunos temos na sala? "))
nomes = []

for x in range(qtd):
    # alu_no = input("Digite o nome do aluno: ")
    # nomes += alu_no
    nomes.append(input("Digite o nome do aluno: "))
for i in range(qtd):
    print(nomes[i])
# for y in nomes:
#     print(y)
