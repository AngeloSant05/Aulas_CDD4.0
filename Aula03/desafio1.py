hora1 = int(input("Digite a hora da entrada: "))
minuto1 = int(input("Digite os minutos da entrada: "))
hora2 = int(input("Digite a hora da outra entrada: "))
minuto2 = int(input("Digite os minutos da outra entrada: "))

if hora1 > 12:
    hora1 = hora1 - 12
if hora2 > 12:
    hora2 = hora2 - 12

hora_t = hora1 + hora2
minuto_t = minuto1 + minuto2

if minuto_t >= 60:
    minuto_t = minuto_t - 60
    hora_t = hora_t + 1
if hora_t > 12:
    hora_t = hora_t - 12

if minuto_t < 10:
    print(f"São {hora_t}:0{minuto_t}")
else:
    print(f"São {hora_t}:{minuto_t}")
