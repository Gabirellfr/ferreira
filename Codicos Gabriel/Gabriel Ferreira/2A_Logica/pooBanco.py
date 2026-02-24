import os
os.system('clear || cls')

class ContaBancaria:
  def __init__(self, saldo_inicial):
    self.__saldo = saldo_inicial
  def get_saldo(self):
    return self.__saldo 
  def depositar(self, deposito):
    self.__saldo = self.__saldo + deposito 
# Uso da classe
conta = ContaBancaria(1000000)
conta.depositar(500000)
print(conta.get_saldo())  