# Variáveis
nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
salario = float(input("Digite o seu salário: "))
aumento = float(input("Digite a porcentagem que deseja aumentar: "))
sal_aum = (salario * (aumento/100)) + salario
filho = int(input("Quantos filhos você tem?\n"))
abono = 150 * filho
total = abono + sal_aum
ferias = sal_aum /3
total2 = sal_aum + ferias + abono
imp_renda = total2 - (sal_aum * 0.15)
inss = imp_renda - (sal_aum * 0.8)

# Print
print(
    f"Olá {nome} essa é a sua idade {idade} anos.\nE esse é o seu salário R${salario}."
    f"\nE esse é o seu salário com o aumento de {aumento}%: R${sal_aum}."
    f"\nE esse é o valor que sobrará para você R${inss}")
