class ContaBancaria:

    def __init__(self, num_c, saldo, status_c, nome_c, tipo_c):
        self.numconta = int(num_c)
        self.saldo = float(saldo)
        self.statusconta = status_c
        self.nomeconta = nome_c
        self.tipoconta = tipo_c

    def depositar(self):
        if self.statusconta == "ativa" or self.statusconta == "ATIVA" or self.statusconta == "Ativa":
            deposito = float(input("Quanto você deseja depositar?\n"))
            self.saldo += deposito
            print(f"Deposito efetuado com sucesso.\n"
                  f"Você possui R${self.saldo} em sua conta.")
        else:
            print("Por favor ative sua conta antes de usar.")

    def sacar(self):
        if self.statusconta == "ativa" or self.statusconta == "ATIVA" or self.statusconta == "Ativa":
            saque = float(input("Quanto você deseja sacar?\n"))
            if self.saldo - saque >= 0:
                self.saldo -= saque
                print(f"Saque efetuado com sucesso.\n"
                      f"Você possui R${self.saldo} em sua conta.")
            else:
                print("Saldo insuficiente.")
        else:
            print("Por favor ative sua conta antes de usar.")

    def versaldo(self):
        if self.statusconta == "ativa" or self.statusconta == "ATIVA" or self.statusconta == "Ativa":
            print(f"Olá {self.nomeconta}, você possui R${self.saldo} na conta.")
        else:
            print("Por favor ative sua conta antes de usar.")

    def ativarconta(self):
        if self.statusconta == "ativa" or self.statusconta == "ATIVA" or self.statusconta == "Ativa":
            print(f"{self.nomeconta} sua conta já está ativa.")
        else:
            print("Conta ativada com sucesso!")
            self.statusconta = self.statusconta.replace('Desativada', 'ativa')

    def desativarconta(self):
        if self.statusconta != "ativa" or self.statusconta != "ATIVA" or self.statusconta != "Ativa":
            if self.saldo == 0:
                print("Conta desativada com sucesso!")
            else:
                print("Para desativar a conta primeiro zere o seu saldo.")
        else:
            print("Sua conta já está desativada")


p1 = ContaBancaria(0000, 500, "Ativa", "Lorenna", "Corrente")
# p1.depositar()
# p1.sacar()
# p1.versaldo()
# p1.ativarconta()
# p1.desativarconta()

p2 = ContaBancaria(6960, 2000, "Ativa", "Ângelo", "Poupança")
# p2.depositar()
# p2.sacar()
# p2.versaldo()
# p2.ativarconta()
# p2.desativarconta()
