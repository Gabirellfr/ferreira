import os
os.system('cls | clear')

# def recomendar_sala(participantes, tipo):
#   if (participantes <= 5) and (tipo == 'normal'):
#     print('Você deve utilizar a sala pequena')
#   elif (participantes >= 6 and participantes <= 15) and (tipo == 'normal'):
#     print('Você deve utilizar a sala média')   
#   else:
#     print('Você deve utilizar a sala grande')  

# participante = int(input('Quantos participantes?'))
# tipo = str(input('Qual o tipo de reunião'))
# recomendar_sala(participante, tipo)      

def recomendar_sala(numero_pessoas, tipo_reuniao):
  if (numero_pessoas <= 5) and (tipo_reuniao == 'normal'):
    return('Sala pequena')
  elif (numero_pessoas >= 6 and numero_pessoas<=15) and (tipo_reuniao == 'normal'):
    return('Sala média')
  else:
    return('Sala grande')

print(recomendar_sala(4, 'normal'))
