pontuacao1 = 0
pontuacao2 = 0

while pontuacao1 != 3 and pontuacao2 != 3:
    print("Digite:"
          "\n[0] para Pedra"
          "\n[1] para Papel"
          "\n[2] para Tesoura")
    jogador1 = input("Jogador 1 insira sua escolha: ")
    while jogador1 != "0" and jogador1 != "1" and jogador1 != "2":
        jogador1 = input("Jogada inválida. Digite novamente: ")
    else:
        jogador2 = input("Jogador 2 insira sua escolha: ")
        while jogador2 != "0" and jogador2 != "1" and jogador2 != "2":
            jogador2 = input("Jogada inválida. Digite novamente: ")
        else:
            if jogador1 == jogador2:
                print("Empate!")
            else:
                if jogador1 == "0":
                    if jogador2 == "1":
                        print("\nJogador 2 ganhou a rodada.\n")
                        pontuacao2 += 1
                    else:
                        print("\nJogador 1 ganhou a rodada.\n")
                        pontuacao1 += 1
                if jogador1 == "1":
                    if jogador2 == "0":
                        print("\nJogador 1 ganhou a rodada.\n")
                        pontuacao1 += 1
                    else:
                        print("\nJogador 2 ganhou a rodada.\n")
                        pontuacao2 += 1
                if jogador1 == "2":
                    if jogador2 == "0":
                        print("\nJogador 2 ganhou a rodada.\n")
                        pontuacao2 += 1
                    else:
                        print("\nJogador 1 ganhou a rodada.\n")
                        pontuacao1 += 1

if pontuacao1 == 3:
    print("Jogador 1 venceu a partida.")
else:
    print("Jogador 2 venceu a partida.")
