comeco = int(input("Digite a hora inicial: "))
fim = int(input("Digite a hora final: "))

total_hora = fim - comeco

if total_hora == 0:
    print("O jogo de Xadrez durou 24 horas.")
elif total_hora > 0:
    print(f"O jogo de Xadrez durou {total_hora} horas")
else:
    print(f"O jogo de Xadrez durou {total_hora + 24} horas")