import random #biblioteca de sorteio
import os #biblioteca para o CMD

os.system('clear || cls') #função que escreve algo no cmd

palpite = 101
numeroMisterioso = random.randint(1,100) #armazena o número misterioso
contador = 0
while (palpite != numeroMisterioso):
  contador = contador + 1
  palpite = int(input('Tente acertar o número misterioso '))
  if (palpite < numeroMisterioso):
    print('O número misterioso é maior\n')
  elif (palpite > numeroMisterioso):
    print('O número misterioso é menor\n')
  else:
    print('Você acertou o número misterioso\nParabéns você ganhou o jogo em', contador, 'tentativas')
    
  