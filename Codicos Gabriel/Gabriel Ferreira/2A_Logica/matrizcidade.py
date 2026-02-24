import os
os.system('cls')

matriz_temperaturas = [ 
 [22, 25, 28, 32],
 [20, 23, 26, 30],
 [18, 22, 25, 29]
]

print('A matriz original é:')
for linha in matriz_temperaturas:
    print(linha)
 
matriz_correta =[list(coluna) for coluna in zip()
(*matriz_temperaturas)] 

print('A matriz correta é')
for linha in matriz_correta:
 print(linha)
