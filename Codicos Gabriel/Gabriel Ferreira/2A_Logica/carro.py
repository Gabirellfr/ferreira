# class Carro:
#   def __init__(self, marca, modelo, ano, cor, preço):
#     self.__marca = marca
#     self.__modelo = modelo
#     self.__ano = ano
#     self.__cor = cor
#     self.__preço = preço
#   def get_marca(self):
#     return self.__marca
#   def set_marca(self, nova_marca):
#     self.__marca = nova_marca
#   def get_modelo(self):
#     return self.__modelo
#   def set_modelo(self, nova_modelo):
#     self.__modelo = nova_modelo
  
# ft = Carro('fiat', 'weekend adventure ', 2015, 'PRETO', 'R$ 45.000') #iniciando o objeto ft
# print(ft.get_marca()) # mostra a marca do objeto ft
# ft.set_marca('chevrolet') # atualiza a marca do objeto ft
# print(ft.get_marca()) #mostra a marca atualizada


# Classe Carro
class Carro:
    def __init__(self, marca, modelo, ano):
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano

    # Getters
    def get_marca(self):
        return self.__marca

    def get_modelo(self):
        return self.__modelo

    def get_ano(self):
        return self.__ano

    # Setters
    def set_marca(self, nova_marca):
        self.__marca = nova_marca

    def set_modelo(self, novo_modelo):
        self.__modelo = novo_modelo

    def set_ano(self, novo_ano):
        self.__ano = novo_ano

    def __str__(self):
        return f"{self.__marca} {self.__modelo} ({self.__ano})"


# Classe Estoque
class Estoque:
    def __init__(self):
        self.__carros = []  # Lista privada de carros

    def adicionar_carro(self, carro):
        self.__carros.append(carro)
        print(f"Carro {carro.get_marca()} {carro.get_modelo()} adicionado ao estoque.")

    def listar_carros(self):
        if not self.__carros:
            print("O estoque está vazio.")
        else:
            print("\nCarros em estoque:")
            for i, carro in enumerate(self.__carros, 1):
                print(f"{i}. {carro}")


# ----- Testando o sistema -----
if __name__ == "__main__":
    # Criando os carros pedidos
    carro1 = Carro("Volkswagen", "Nivus", 2021)
    carro2 = Carro("Chevrolet", "Corvette", 2015)
    carro3 = Carro("Toyota", "Hilux", 2024)

    # Criando estoque
    estoque = Estoque()

    # Adicionando carros ao estoque
    estoque.adicionar_carro(carro1)
    estoque.adicionar_carro(carro2)
    estoque.adicionar_carro(carro3)

    # Listando os carros
    estoque.listar_carros()