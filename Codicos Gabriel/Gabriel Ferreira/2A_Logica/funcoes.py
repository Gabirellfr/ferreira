import os
os.system('cls || clear')

# def bemVindo():
#   print('Seja bem vindo')
# def bemVindoDeVolta():
#   print('Seja bem vindo de volta')
# bemVindoDeVolta()

# def bemVindo():
#   return 'seja bem vindo'

# def bemVindoDeVolta():
#   return 'seja bem vindo de volta'

# #colocando uma função dentro de um print
# print(bemVindo())

# # Armazenando uma função e uma variável e dando print
# volta = bemVindoDeVolta()
# print(volta)


def bemVindo():
  return 'seja bem vindo'

def bemVindoDeVolta():
  return 'seja bem vindo de volta'

def verificarCliente(clienteNovo):
  if (clienteNovo):
    return bemVindo()
  else:
    return bemVindoDeVolta()

print(verificarCliente(False))