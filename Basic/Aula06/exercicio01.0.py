primeira_nota = float(input("Digite sua primeira nota: "))
while primeira_nota < 0 or primeira_nota > 10:
    primeira_nota = float(input(f"Valor inválido.\nDigite novamente: "))

segunda_nota = float(input("Digite sua segunda nota: "))
while segunda_nota < 0 or segunda_nota > 10:
    segunda_nota = float(input(f"Valor inválido.\nDigite novamente: "))

media = (primeira_nota + segunda_nota)/2
# if media >= 7:
#     print("Você está aprovado >_<")
# else:
#     if media >= 4:
#         print("Você está de recuperação ¬_¬' ")
#     else:
#         print("Você está reprovado -_-")
print(f"Sua média foi {media}")
