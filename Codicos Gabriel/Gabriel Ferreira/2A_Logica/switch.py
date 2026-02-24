import os
os.system('clear || cls')

# def switch_dia(dia):
#   dias = {
#   1: "Segunda-feira",
#   2: "Terça-feira",
#   3: "Quarta-feira",
#   4: "Quinta-feira",
#   5: "Sexta-Feira"
#   }
#   return dias.get(dia, "Dia inválido")

# dia_selecionado = switch_dia(4)
# print("O dia é:", dia_selecionado)

# def calcular_preco(cafe):
#   precos = {
#   "espresso": 1.50,
#   "latte": 2.00,
#   "cappuccino": 2.25
#   }
#   return precos.get(cafe, "Café não disponível")
# preco = calcular_preco("cappuccino")
# print(preco)

def calcular_multa(livro):
  multas = {
  "ônix": "Chevrolet",
  "não ficção": 0.60,
  "referência": 0,
  "aventura": 0.70
  }
  return multas.get(livro)


preco = calcular_multa("")
print(preco)
