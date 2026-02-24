import os
os.system('cls')

def calcular_distancia():
  intervalos = int(input("quantos intervalos você vai registrar?"))
  soma = 0
  for i in range(1,intervalos+1):
    t = float(input(f'Quanto tempo durou a {i}º corrida?'))
    vm = float(input(f'Qual foi a velocidade média da {i}º corrida?'))
    soma = soma + (vm/(60/(t*60)))
  print(soma)
  
calcular_distancia()