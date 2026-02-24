import os
os.system('clear || cls')

# for variavel in range(5):
#   print(variavel)

# variavel = "Python"
# contador = 0
# for letras in variavel:
#   if (letras == 'a') or (letras == 'e') or (letras == 'i') or (letras == 'o') or (letras == 'u'):
#     contador = contador + 1

# print(f'Tem {contador} vogal(s) na palavra {variavel}')

dados = {"nome":"Alice", "idade": 30}
for chave, valor in dados.items():
  print(f'{chave}: {valor}')
