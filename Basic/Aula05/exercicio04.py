senha = "cdd4.0"
senha_comp = input("Digite sua senha: ")
cont = 1

while senha != senha_comp:
    senha_comp = input("Senha errada.\nTente novamente:")
    cont += 1
    if cont > 3:
        print("Número de tentativas alcançadas.")
        break
else:
    print("Senha correta")
