import os
os.system('clear || cls')

n1 = int(input('Digite o valor 1 '))
n2 = int(input('Digite o valor 2 '))
n3 = int(input('Digite o valor 3 '))

if(n1 > n2 and n1 > n3):
  maior = n1
elif(n2 > n3 and n2 > n1):
  maior = n2
else:
  maior = n3

if(n1 < n2 and n1 < n3):
  menor = n1
elif(n2 < n3 and n2 < n1):
  menor = n2
else:
  menor = n3
  
if(n1 < n2 and n1 > n3):
  meio = n1
elif(n2 < n3 and n2 > n1):
  meio = n2
else:
  meio = n3
print(maior, meio, menor)