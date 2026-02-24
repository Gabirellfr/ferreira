import os
os.system('cls || clear')

#Exemplo 1
# num = int(input("Digite um número: "))
# if num > 0:   
#   if num % 2 == 0:   
#     print("O número é positivo e par.")   
#   else:   
#     print("O número é positivo e ímpar.")   
# elif num < 0:
#   if num % 2 == 0:
#     print("O número é negativo e par.")
#   else:
#     print("O número é negativo e ímpar.")
# else:
#   print("O número é zero.")

nacionalidade = str(input('Digite seu país'))
cargo = str(input('Digite seu cargo'))

if (nacionalidade == "brasil"):
  if (cargo == 'gerente'):
    print('O acesso total ao sistema foi liberado')
  else:
    print('O acesso de brasileiro foi liberado')
else:
  if (cargo == 'gerente'):
    print('O acesso total para estrangeiros foi liberada')
  else:
    print('O acesso limitado a estrangeiros foi liberado')