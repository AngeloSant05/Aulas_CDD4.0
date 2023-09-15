tipo = input("Informe o tipo de combustível: ")
quantidade = float(input("Quantos litros deseja abastecer? "))
total = 0
if tipo == "g":
    total = quantidade*5.8
else:
    total = quantidade*4.9
print(f"Você gastou R${total}")