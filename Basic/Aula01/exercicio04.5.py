# Variáveis
nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
salario = float(input("Digite o seu salário: "))
aumento = float(input("Digite a porcentagem que deseja aumentar: "))
sal_aum = (salario * (aumento/100)) + salario
inss =  sal_aum - (sal_aum * 0.08)
# Print
print(
    f"Olá {nome} essa é a sua idade {idade} anos.\nE esse é o seu salário R${salario}."
    f"\nE esse é o seu salário com o aumento de {aumento}%: R${sal_aum}."
    f"\nO seu salário após o INSS será R${inss}")
