import os 
os.system('clear || cls') 

class Lampada:
  def __init__(self):
    self.estado = True # Começa ligada
  def alterar_estado(self):
    if (self.estado == False):
      self.estado = True
    else:
      self.estado = False
    return(self.estado)
              
lampada = Lampada()
print(lampada.alterar_estado())  # Liga a lâmpada


# from os import system 
# system('clear || cls')
# class bank_account:
#     def _init_(self, saldo, deposite):
#         self.__saldo = saldo
#         self.__deposite = deposite
        
#     def get_saldo(self):
#         return self.__saldo
    
#     def deposite(self):
#         return self.__deposite
    
#     def new_saldo(self):
#         return self.get_saldo()+self.deposite()
    
# conta = bank_account(1000, 500)
# print(conta.get_saldo())
# print(conta.deposite())
# print(conta.new_saldo())
