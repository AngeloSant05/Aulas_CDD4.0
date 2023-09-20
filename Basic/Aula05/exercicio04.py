senha = "cdd4.0"
senha_solic = input("Digite sua senha: ")
cont = 1

while senha != senha_solic:
    senha_solic = input("Senha errada.\nTente novamente: ")
    cont += 1
    if cont >= 3:
        print("Número de tentativas alcançadas.\n       Usuário bloqueado.")
        break
else:
    print("Senha correta")
