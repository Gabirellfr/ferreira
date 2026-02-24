import os
os.system('clear || cls')

numero = int(input('Digite um número para mostrar a tabuada de 1 a 10 '))

for contador in range(1, 11):
  print(f'{numero} x {contador}: {contador * numero}')