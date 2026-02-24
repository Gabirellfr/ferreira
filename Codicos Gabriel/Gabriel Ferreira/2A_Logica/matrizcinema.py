import os
os.system ('cls')

#criar uma matriz 5x8 com todos os assentos livres

assentos = [[0 for c in range(8)] for i in range (5)]

def exibir_mapa():
    print('mapa dos assentos:')
    for linha in assentos:
        print(linha)

def reservar_assento(linha,coluna):
    if assentos[linha][coluna] == 0:
      assentos[linha][coluna] = 1
    print('o assento foi reservado com sucesso!')
def cancelar_assento(linha,coluna):
    if assentos[linha][coluna] == 1:
       assentos[linha][coluna] = 0
    print('acento cancelado com sucessoo')
    
    
      
reservar_assento(3,4)
cancelar_assento(3,4)
exibir_mapa()