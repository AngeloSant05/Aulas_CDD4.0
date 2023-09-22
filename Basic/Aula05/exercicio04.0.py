senha = "cdd4.0"
senha_solic = input("Digite sua senha: ")
tentativas = 1

while senha != senha_solic:
    if tentativas >= 3:
        print("Número de tentativas alcançadas.\n       Usuário bloqueado.")
        break
    tentativas += 1
else:
    print("Senha correta")
