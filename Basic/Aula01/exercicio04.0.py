# Variáveis
nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
salario = float(input("Digite o seu salário: "))
sal_aum = (salario * 0.2) + salario

# Print
print(
    f"Olá {nome} essa é a sua idade {idade} anos.\nE esse é o seu salário R${salario}."
    f"\nE esse é o seu salário com o aumento R${sal_aum}")
