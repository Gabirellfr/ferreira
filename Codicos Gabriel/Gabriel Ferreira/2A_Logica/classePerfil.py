import os
os.system('cls | clear')

class Perfil(object):
  'Classe padrão para perfis de usuário'

  def __init__(self, nome, telefone, empresa):
    self.nome = nome
    self.telefone = telefone
    self.empresa = empresa
    self.curtidas = 0

  def imprimir(self):
    print(f'Nome : {self.nome},  Telefone: {self.telefone}; Empresa {self.empresa}')

perfil = Perfil('Flávio Almeida', 'não informado', 'Caelum')
print(perfil.curtidas)
  