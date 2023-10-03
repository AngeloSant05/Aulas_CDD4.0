notas = [0, 0, 0, 0, 0]
nota_total = 0

for x in range(5):
    notas[x] = (float(input(f"Digite sua {x+1}ª nota: ")))

for y in range(5):
    nota_total += notas[y]

media = nota_total / 5

for z in range(5):
    if notas[z] >= media:
        print(f"A nota {notas[z]} foi maior ou igual a média {media}")
