'''
Escreva um algoritmo para ler a hora de
início e a hora de fim de um jogo de Xadrez
(considere apenas horas inteiras, sem os
minutos) e calcule a duração do jogo em
horas, sabendo-se que o tempo máximo de
duração do jogo é de 24 horas e que o jogo
pode iniciar em um dia e terminar no dia
seguinte
'''

comeco = int(input("Digite a hora inicial: "))
fim = int(input("Digite a hora final: "))

total_hora = fim - comeco

if total_hora == 0:
    print("O jogo de Xadrez durou 24 horas.")
elif total_hora > 0:
    print(f"O jogo de Xadrez durou {total_hora} horas")
else:
    print(f"O jogo de Xadrez durou {total_hora + 24} horas")


