ano_atual = int(input("Em que ano estamos: "))
mes_atual = int(input("Em que mês estamos: (1 à 12) \n"))
mes_nascimento = int(input("Digite o mês que você nasceu: (1 à 12) \n"))
idade = int(input("Digite sua idade: "))

if mes_atual >= mes_nascimento:
    nascimento = ano_atual - idade
else:
    nascimento = ano_atual - idade - 1
print(f"Você nasceu em {nascimento}.")
