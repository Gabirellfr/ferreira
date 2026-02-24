import os
os.system('clear || cls')

sigla = str(input('Digite a sigla do elemento')).capitalize()

if (sigla == 'Ti'):
  print('Nome: Titânio\nNúmero Atômico: 22\nMassa: 47,87')
elif (sigla == 'Fe'):
  print('Nome: Ferro\nNúmero Atômico: 26 \nMassa: 55,84')
else:
  print('Esta sigla não existe ou não está na base de dados')
