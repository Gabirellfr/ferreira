import os
os.system('clear || cls')

def fazer_pedido():
  tempos = {
  'hamburguer': 5,
  'batata-frita': 5,
  'nuggets': 3,
  'calabresa':2,
  'salada': 2
  }
  
  horario = 19
  
  pedido = str(input('Digite o lanche desejado \n'))
  
  tempo_base = tempos.get(pedido, 10)
  
  acompanhamento = str(input('Você quer o lanche com acompanhamentos? (s/n)\n'))
  if(acompanhamento.upper() == 'S'):
    tempo_base+=5
    
  if horario in range(12, 15) or horario in range(19, 22):
    tempo_base+=5
    
  return tempo_base

tempo = fazer_pedido()
print('O tempo total para realizar seu pedido é de:',tempo,'minutos')