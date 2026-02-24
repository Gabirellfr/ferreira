import random
import os #não precisa
os.system('clear || cls') #não precisa
numeroSecreto = random.randint(1, 4)
palpite = 51
tentativas = 5
while (palpite != numeroSecreto and tentativas>0):
  palpite = int(input('Digite um número como tentativa'))
  if (palpite == numeroSecreto):
    print('Parabéns você acertou o número secreto')
  elif(palpite > numeroSecreto):
    print('O número secreto é menor')
    tentativas = tentativas - 1
  else:
    print('O número secreto é maior') 
    tentativas = tentativas - 1 
  if(tentativas == 0):
    print('Suas tentativas acabaram\nO número secreto era',numeroSecreto)
  