numero = 1500
encontrado = False

while 1500 <= 2700 and not encontrado:
    if numero % 5 == 0 and numero % 7 == 0:
        print(f"O primeiro número divisível por 5 e 7 entre 1500 e 2700 é: {numero}")
        encontrado = True
    numero += 1
