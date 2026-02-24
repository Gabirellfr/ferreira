import os

os.system('cls || clear')

# numero = int(input('Digite um número '))

# if (numero>0):
#   print(f'O número {numero} é positivo')
# elif (numero<0):
#   print(f'O número   {numero} é negativo')
# else:
#   print(f'O número {numero} é zero')

#Exer 2
# numero1 = int(input('Digite o primeiro número'))
# numero2 = int(input('Digite o segundo número'))
# if (numero1 > numero2):
#   print(f'O número {numero1} é o maior')
# elif(numero2 > numero1):
#   print(f'O número {numero2} é o maior')
# else:
#   print('Os números são iguais')

#Exer 3
# numero = int(input('Digite um número'))
# if(numero%2==0):
#   print('O número é par')
# else:
#   print('O número é ímpar')

#Exer 4
# numero = int(input('Digite um número'))
# if (numero%5==0 and numero%3==0):
#   print(f'O número {numero} é divisível')
# else:
#   print(f'O número {numero} não é divisível')

#Exer5 
# numero = 1  
# while (numero!=0):
#   numero = int(input('Digite um número'))
# print('O laço foi encerrado')

#Exer 6
# numero = int(input('Digite um número'))
# for i in range(1, 11):
#   print(f'{numero} x {i} = {numero*i}')

#Exer 7
# numero = int(input('Digite um número'))
# contaPrimo = 0
# for i in range(1, numero+1):
#   if (numero%i==0):
#     contaPrimo = contaPrimo +  1 
# if (contaPrimo<=2):
#   print(f'O número {numero} é primo')
# else:
#   print(f'O número {numero} não é primo')

#Exer 8
# for i in range (0, 101):
#   if (i % 2 == 0):
#     print(i)

#Exer 9
# soma = 0
# while (soma<=100):
#   numero = int(input('Digite o número a ser somado'))
#   soma = soma + numero
#   print(f'A soma está em {soma}\n')
# print('A soma ultrapassou 100')

#Exer 10
# vogal = ['a', 'e', 'i', 'o', 'u']
# letra = str(input('Digite uma letra: '))
# if(letra in vogal):
#   print(f'A letra {letra} é uma vogal')
# else:
#   print(f'A letra {letra} é uma consoante')

# nota = float(input('Digite sua nota'))
# if(nota>=7):
#   print('Aprovado')
# elif(nota>=5 and nota<=6.9):
#   print('Em recuperação')
# else:
#   print('Reprovado')