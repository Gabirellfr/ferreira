
T = int(input())


numeros = [0] * 61  


numeros[0] = 0
numeros[1] = 1


for i in range(2, 61):
    numeros[i] = numeros[i-1] + numeros[i-2]


for _ in range(T):
    N = int(input())
    print(f"Posicao {N} = {numeros[N]}")
