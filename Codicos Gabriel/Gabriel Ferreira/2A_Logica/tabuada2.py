import os
os.system('cls || clear')
numero = int(input('Digite o número para tabuada'))

for contador in range(1,11):
  print(numero,'x', contador, '=', numero*contador)