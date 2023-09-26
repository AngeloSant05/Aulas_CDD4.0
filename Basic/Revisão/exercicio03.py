ano_atual = int(input("Em que ano estamos: "))
mes_atual = int(input("Em que mês estamos: (1 à 12) \n"))
mes_nascimento = int(input("Digite o mês que você nasceu: (1 à 12) \n"))
idade = int(input("Digite sua idade: "))

nascimento = ano_atual - idade

if mes_atual >= mes_nascimento:
    print(f"Você nasceu em {nascimento}.")
else:
    print(f"Você nasceu em {nascimento - 1}.")
