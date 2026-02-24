import os #não precisa
import random
os.system('clear || cls') #não precisa

aleatorio = random.randint(1, 100)
tentativa = 0
contador = 0

while (tentativa != aleatorio):
  contador = contador + 1 # contador=+1
  tentativa = int(input('Tente acertar o número aleatório entre 1 100:\n'))
  if (tentativa > aleatorio):
    print(f'O número misterioso é menor que {tentativa}')
  elif (tentativa == aleatorio):
    print('Você acertou o número misterioso! Parabéns')
    print(f'Você ganhou em {contador} tentativas')
  elif (tentativa < aleatorio):
    print(f'O número misterioso é maior que {tentativa}')
  else:
    print('Este não é um número válido')

