# 1. Criação de uma lista vazia
numeros = []

# Adicionando o valor 10 ao vetor numeros c a func append
# Vamos adicionar 5 números
numeros.append(10)  # adiciona 10
numeros.append(5)   # adiciona 5
numeros.append(8)   # adiciona 8
numeros.append(20)  # adiciona 20
numeros.append(15)  # adiciona 15

#Mostrar a lista atual:
print("Lista inicial:", numeros)

#Remove o valor 5 da lista
numeros.remove(5)

#Mostrar lista sem o 5
print("Lista sem o 5:", numeros)

#Mostrar a soma dos elementos
soma = sum(numeros)
print("Soma dos elementos:", soma)

#Calcular a média
media = sum(numeros)/ len(numeros)
print('A média da lista números é ', media)

#Ordernar do menor para o maior
numeros.sort()
print('A lista ordenada é', numeros)