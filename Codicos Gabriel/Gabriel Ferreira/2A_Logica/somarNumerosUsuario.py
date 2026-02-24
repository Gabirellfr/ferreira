# Use um laço while para somar números digitados pelo usuário até que a soma ultrapasse 100.

import os 
os.system('cls || clear')
soma = 0
while (soma <= 100):
  numero = float(input('Digite um número '))
  soma = soma + numero
  print(f'A soma está em {soma}')

print('A soma ultrapassou 100\nFIM')
  