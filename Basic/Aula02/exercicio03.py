time1 = input("Digite o nome do seu time: ")
gols1 = int(input("Quantos gols o time 1 fez? "))
time2 = input("Digite o nome de outro time: ")
gols2 = int(input("Quantos gols o time 2 fez? "))

if gols1 == gols2:
    print("O jogo empatou.")
else:
    if gols1 > gols2:
        print(f"O {time1} ganhou!")
    else:
        print(f"O {time2} ganhou!")
