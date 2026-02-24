import os
os.system('cls || clear')

# palavra = str(input('Qual a palavra desejada '))

# vogais = ["a", 'e', 'i', 'o', 'u']
# contador = 0
# for letra in palavra:
#   print(letra)
#   if (letra in vogais):
#     contador = contador + 1
# print(f'O número de vogais dentro de Python é {contador}')


# sobremesa = {
#   1: "Torta de Limão",
#   2: "Brigadeiro",
#   3: "Doce de Leite",
#   4: "Torta de Morango",
#   5: "Sorvete"
# }
# print('Nosso cardápio, possui:' )
# for numero, doce in sobremesa.items():
#   print(f'{numero}:{doce}')

# print([x**30 for x in range(10)]) 

matriz = [[1, 2], [3, 4]]
for linha in matriz:
  for elemento in linha:
   print(elemento)