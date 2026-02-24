import os
os.system ('cls')
#Crie um arquivo no vscode com nome de vetorRevisao.py

#Pegar o valor da primeira posição
valor = int(input('Digite um valor\n'))

#Inicializar o vetor 'n' com 10 espaços vazios (0)
n = [0] * 20 # n = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Atribuindo o número da variável valor ao vetor 'n'
n[0] = valor # n = [valor, 0, 0, 0, 0, 0, 0, 0, 0, 0]


for valores in range(1, 20):
    n[valores] = n[valores - 1] * 2 #Pega a posição anterior, multiplica e atribui à atual

# Mostra o vetor inteiro
print(n)
