import os
os.system ('cls')
def pode_acessar(cargo, dia_semana):
    dias_uteis = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira"]

    cargo = cargo.strip().lower()
    dia_semana = dia_semana.strip().lower()

    # Gerentes têm acesso irrestrito
    if cargo == "gerente":
        return True
    # Analistas e Estagiários têm acesso apenas em dias úteis
    elif cargo in ["analista", "estagiário"] and dia_semana in dias_uteis:
        return True
    else:
        return False


# Teste do programa
cargo = input("Digite o cargo do funcionário: ")
dia_semana = input("Digite o dia da semana: ")

if pode_acessar(cargo, dia_semana):
    print("Acesso Permitido.")
else:
    print("Acesso Negado.")
