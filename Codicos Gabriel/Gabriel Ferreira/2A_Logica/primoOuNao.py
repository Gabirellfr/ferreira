import os
os.system('clear || cls')

numero = int(input('Digite o número'))
contador = 0
for i in range(1,numero+1):
  if (numero%i==0):
    print(f'O número{numero} é dívisível por {i}')
    contador = contador + 1  

if (contador > 2):
  print(f' O número {numero} não é primo')  
else:
  print(f' O número {numero} é primo')  