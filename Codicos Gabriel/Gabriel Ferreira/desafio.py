import os
os.system('cls')

def sequencia_logica(n):
    for i in range(1, n+1):
        print(i, i**2, i**3)
        print(i, i**2 + 1, i**3 + 1)

# Exemplo de uso
N = int(input())
sequencia_logica(N)