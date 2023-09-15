# Variáveis

aluno = input("Digite o nome do aluno: ")
print(f"Vamos calcular a média de {aluno}")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = (nota1 + nota2 + nota3) / 3
if media >= 7:
    print(f"Parabéns {aluno}, você foi aprovado!"
          f"\nSua média foi {media}")
else:
    print(f"Que pena {aluno}, você foi reprovado!"
          f"\nSua média foi {media}")


