import os
os.system('clear || cls')

# class Funcionario:
#   def __init__(self, nome, salario):
#     self.nome = nome
#     self.__salario = salario # PROBLEMA: Salário acessível publicamente

# func = Funcionario("João", 5000)
# func.salario -=1000 # Modificação indevida do salário
# func.salario.set()
# print(func.salario)

class Funcionario:
  def __init__(self, nome, salario):
    self.nome = nome
    self.__salario = salario  # Atributo privado

  def set_salario(self, novo_salario):
    self.__salario = novo_salario

  def get_salario(self):
    return self.__salario

func = Funcionario("João", 5000)
func.set_salario(func.get_salario() + 1000)  # Modificação via setter
print(func.get_salario())
