nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

if nota1 < 0 or nota2 < 0 or nota3 < 0 or nota1 > 10 or nota2 > 10 or nota3 > 10:
    print("Notas inválidas.")
else:
    media = (nota1 + nota2 + nota3) / 3
    if media >= 7:
        print("Você foi aprovado!")
    else:
        if media >= 4:
            print("Você está de recuperação.")
        else:
            print("Que pena, você foi reprovado ;-;")
