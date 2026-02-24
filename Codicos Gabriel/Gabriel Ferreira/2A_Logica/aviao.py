import os
os.system('cls')

def campeonato(competidores, papel, distribuicao):
    if ((competidores * distribuicao) <= papel):
        return "é suficiente"
    else:
        return "não é suficiente"

escolaVicente = campeonato(100, 300, 2)

print(f'Vicente: {escolaVicente}')

escolaLeila = campeonato(100, 300, 2)

print(f'Leila: {escolaLeila}')