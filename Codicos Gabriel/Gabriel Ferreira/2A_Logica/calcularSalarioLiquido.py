import os
os.system('cls || clear')

valorAula = float(input('Digite o valor da hora aula'))
numeroAula = float(input('Digite quantas aulas você passa no mês'))
inss = float(input('Digite o percentual de desconto no inss'))
bruto = (valorAula*numeroAula)
liquido = bruto - ((bruto*inss)/100)

print(f'Seu salário líquido é {liquido}')