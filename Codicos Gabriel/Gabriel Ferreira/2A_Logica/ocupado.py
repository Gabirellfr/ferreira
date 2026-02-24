import os
os.system('cls')

predio = ['ocupado', 'vazio', 'ocupado', 'ocupado', 'vazio', 'ocupado', 'vazio']

contador = 0
for status in predio:
    if status == 'ocupado':
        contador += 1

print(contador)
