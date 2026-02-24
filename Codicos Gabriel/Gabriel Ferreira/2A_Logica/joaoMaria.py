import os
os.system('clear || cls')

maria = 150
joao = 140
contador = 0
while (joao <= maria):
  joao = joao + 3
  maria = maria + 2
  contador = contador + 1
  print(f'Ano {contador}\nJoão tem:{joao} cm')
  print(f'Maria tem:{maria} cm\n')
print(f'Passaram {contador} anos para João passar a Maria')


