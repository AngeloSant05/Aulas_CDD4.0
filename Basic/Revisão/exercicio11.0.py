dia = int(input("Que dia é hoje? "))
dia_nasc = int(input("Que dia você nasceu? "))

mes = int(input("Em que mês estamos? "))
mes_nasc = int(input("Em que mês você nasceu? "))

idade = int(input("Qual sua idade? "))

dia_total = dia - dia_nasc
mes_total = mes - mes_nasc
total = idade * 365 + mes_total * 30 + dia_total
print(total)
