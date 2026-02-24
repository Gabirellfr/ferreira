import os
os.system ('cls')

vendas_mensais = [120, 130, 140, 150, 160, 170, 160, 150, 140, 130, 120, 110]

def calcular_total():
    print(sum(vendas_mensais))

def calcular_media():
    print(sum(vendas_mensais)/len(vendas_mensais))

def calcular_maximo():
  maior_valor = max(vendas_mensais)
  localizaçao_maior_valor = vendas_mensais.index(maior_valor)
  print('o mes com maior numero de vendas foi o mes',localizaçao_maior_valor+1)
calcular_maximo()