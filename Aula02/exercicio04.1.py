tipo = input("Informe o tipo de combustível: ")
quantidade = float(input("Quantos litros deseja abastecer? "))
total = 0
if tipo == "g" or tipo == "G":
    total = quantidade*5.8
    print(f"Você gastou R${total}")
else:
    if tipo == "e" or tipo == "E":
        total = quantidade*4.9
        print(f"Você gastou R${total}")
    else:
        print("Tipo de combustível inválido!")
