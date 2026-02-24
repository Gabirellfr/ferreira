class ContaBancaria:
    def __init__(self, numero_conta, saldo=0):
        self._numero_conta = numero_conta
        self._saldo = saldo
        self._numero_transacoes = 0
        self._historico = []

    def get_numero_conta(self):
        return self._numero_conta

    def registrar_transacao(self, descricao, valor):
        self._historico.append(f"{descricao}: R${valor:.2f}")
        self._numero_transacoes += 1

    def transferir(self, valor, conta_destino):
        if not isinstance(conta_destino, ContaBancaria):
            print("Conta de destino inválida.")
            return

        if valor <= 0:
            print("Valor da transferência deve ser positivo.")
            return

        if self._saldo >= valor:
            self._saldo -= valor
            self.registrar_transacao("Transferência Enviada", valor)

            conta_destino._saldo += valor
            conta_destino.registrar_transacao("Transferência Recebida", valor)

            print(f"Transferência de R${valor:.2f} realizada com sucesso "
                  f"para a conta {conta_destino.get_numero_conta()}.")
        else:
            print("Saldo insuficiente para realizar a transferência.")