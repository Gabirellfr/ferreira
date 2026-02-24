import os 
os.system('clear || cls')

frutas = ['maçã', 'uva', 'pêra', 'laranja', 'fruta do conde']
print(frutas[0]) #o index 0 é o 1º item (maçã)
print(frutas[-1]) #- traz a lista do inverso, começa em 1
frutas.append('melancia') #adiciona um valor à lista 
del frutas[2] #apaga de acordo com o index
print(frutas) #mostra a lista inteira sem formatação
frutas.remove('uva') #remove um item pelo seu valor
fruta1 = frutas.pop(0) #pega o último item de frutas e adiciona na variável fruta1
print(fruta1)
