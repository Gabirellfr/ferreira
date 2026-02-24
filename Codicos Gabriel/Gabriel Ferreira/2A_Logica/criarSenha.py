import os
os.system('cls || clear')

# senha = str(input('Digite uma nova senha\n'))
# valido = (senha.isalpha() == False) and (senha.isdigit() == False) and (len(senha) >= 8)
# while valido == False:
#     print('Sua senha não possui o mínimo de 8 caracteres ou não contém números e letras')
#     senha = str(input('Digite uma nova senha\n'))
#     valido = (senha.isalpha() == False) and (senha.isdigit() == False) and (len(senha) >= 8)
# print('Sua senha foi cadastrada com sucesso!')

# Exer 1
# numero = float(input('Digite um número: '))
# if (numero > 0):
#     print(f'O número {numero} é positivo')
# elif (numero < 0):
#     print(f'O número {numero} é negativo')   
# else:
#     print('O número é nulo')

#Exer2
# numero1 = float(input('Digite o primeiro número'))
# numero2 = float(input('Digite o segundo número'))
# if (numero1 > numero2):
#     print(f'O número {numero1} é o maior')
# elif (numero1 < numero2):
#     print(f'O número {numero2} é o maior')
# else:
#     print('Os números são iguais')

#Exer 3
# numero = float(input('Digite um número'))

# if (numero % 2 == 0):
#     print(f'O número {numero} é par')
# else:
#     print(f'O número {numero} é ímpar')

# numero = int(input('Digite um número '))
# if (numero % 3 == 0) and (numero % 5 == 0):
#     print(f'O número {numero} é divisível por 3 e 5')
# else:
#     print(f'O número {numero} não é divisível por 3 e 5')   

# numero = int(input('Digite um número'))

# while (numero != 0):
#     numero = int(input('Digite um número '))
# print('Você digitou 0\n FIM')

numero = int(input('Digite o número da tabuada: '))
for contador in range(1, 11):
    print(f'{numero} x {contador} = {numero*contador}')