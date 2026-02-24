import os
os.system('cls')

def corredor(corrida, pista):
    if (corrida<=pista):
        return(f'O corredor deve deixar a garrafa nos {corrida} metros')
    else:
        return(f'O corredor deve deixar a garrafa nos {(corrida-pista)} metros')

pista_interlagos = corredor(10, 15)
pista_stoamaro = corredor(8, 15)

print(pista_interlagos)
print(pista_stoamaro)
