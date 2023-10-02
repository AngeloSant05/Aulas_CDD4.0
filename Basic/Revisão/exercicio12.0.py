# Escreva um algoritmo para ler o
# número total de eleitores de um
# município, o número de votos brancos,
# nulos e válidos. Calcular e escrever o
# percentual que cada um representa em
# relação ao total de eleitores.

eleitores = int(input("Digite a quantidade de eleitores: "))

branco = 0
valido = 0
nulo = 0

for x in range(eleitores):
    voto = input("Digite seu voto: (0 para branco, 1 para válido, x para nulo) ")
    if voto == "0":
        branco += 1
    elif voto == "1":
        valido += 1
    else:
        nulo += 1

total_branco = (branco * 100) / eleitores
total_valido = (valido * 100) / eleitores
total_nulo = (nulo * 100) / eleitores

print(f"Os dados obtidos com a votação foram os seguintes:"
      f"\n{total_valido}% de votos válidos; "
      f"\n{total_branco}% de votos em branco;  "
      f"\n{total_nulo}% de votos nulos.")