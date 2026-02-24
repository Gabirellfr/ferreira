class ContaBancaria:
    def __init__(self, numero_conta, saldo=0, numero_transacoes=0):
            self.numero_conta = numero_conta
            self.saldo = saldo
            self.numero_transacoes = numero_transacoes
    def depositar(self, valor):
            self.saldo += valor
            self.numero_transacoes += 1