import os
os.system('cls || clear')
senhaCorreta = "eunaosei"
tentativa = 3
while (tentativa > 0):
  senha = str(input('Digite a senha correta '))
  tentativa = tentativa - 1
  if senha == senhaCorreta:
    print('Você acertou sua senha')
    break
  print('Senha incorreta')