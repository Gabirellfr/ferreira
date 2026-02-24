import os
os.system('cls | clear')

def consumo():
  distancia = int(input('Qual foi a distância percorrida?'))
  combustivel = float(input('Qual foi a quantidade gasta de combustível?'))
  print(f'O consumo do carro é de {(distancia/combustivel):.3f} km/l')

consumo()

