import os
os.system('cls || clear')

from abc import ABC, abstractmethod
#importando biblioteca ABC que permite criar superclasses e  reutilização de métodos

#Criando classe Abstrata (base)
class Veiculo (ABC):
  @abstractmethod
  def calcularTempoEntrega(self, distancia):
    pass

#Criação classe derivada Carro
class Carro (Veiculo):
  def calcularTempoEntrega(self, distancia):
    return distancia / 60 #Velocidade média 60km/h

class Caminhao (Veiculo):
  def calcularTempoEntrega(self, distancia):
    return distancia / 40 #Velocidade média 40km/h

class Bicicleta (Veiculo):
  def calcularTempoEntrega(self, distancia):
    return distancia / 15 #Velocidade média 15km/h

def main():
  carro = Carro()
  caminhao = Caminhao()
  bicicleta = Bicicleta()

  distancia = 15 #distancia em km da entrega

  tempo_carro = carro.calcularTempoEntrega(distancia)
  tempo_caminhao = caminhao.calcularTempoEntrega(distancia)
  tempo_bicicleta = bicicleta.calcularTempoEntrega(distancia)

  print(f'Tempo de entrega com Carro: {tempo_carro:.2f} horas')
  print(f'Tempo de entrega com Caminhao: {tempo_caminhao:.2f} horas')
  print(f'Tempo de entrega com Bicicleta: {tempo_bicicleta:.2f} horas')

main()