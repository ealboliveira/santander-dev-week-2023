class Banco:
    def __init__(self):
        self.saldo = 0
        self.depositos = []
        self.saques = []

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            self.depositos.append(valor)
            print(f'Depósito de R$ {valor:.2f} realizado com sucesso.')
        else:
            print('Valor de depósito inválido.')

    def saque(self, valor):
        if valor <= 500 and len(self.saques) < 3:
            if self.saldo >= valor:
                self.saldo -= valor
                self.saques.append(valor)
                print(f'Saque de R$ {valor:.2f} realizado com sucesso.')
            else:
                print('Saldo insuficiente para realizar o saque.')
        else:
            print('Limite de saques diários atingido ou valor de saque excede o limite de R$ 500.')

    def extrato(self):
        if not self.depositos and not self.saques:
            print('Não foram realizadas movimentações e saldo.')
        else:
            print('Extrato:')
            print('Depósitos:')
            for deposito in self.depositos:
                print(f'Depósito de R$ {deposito:.2f}')
            print('Saques:')
            for saque in self.saques:
                print(f'Saque de R$ {saque:.2f}')
            print(f'Saldo: R$ {self.saldo:.2f}')

banco = Banco()
banco.deposito(1000)
banco.saque(300)
banco.saque(200)
banco.saque(600)
banco.extrato()
