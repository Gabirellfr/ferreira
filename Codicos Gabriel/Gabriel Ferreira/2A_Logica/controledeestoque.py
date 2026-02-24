import os
os.system('cls')
 
# Vetor inicial de estoque
estoque = [20, 15, 10, 30, 5]

# Função para vender produtos
def vender(produto, quantidade):
    estoque[produto] -= quantidade

# Função para adicionar produtos
def adicionar(produto, quantidade):
    estoque[produto ] += quantidade

# Função para exibir estoque
def exibirEstoque():
    print("Estoque atual:", estoque)

# Executando as operações
exibirEstoque()
vender(0, 10)
exibirEstoque()
vender(1, 5)
exibirEstoque()
vender(3, 15)
exibirEstoque()
adicionar(3, 100)
exibirEstoque()
adicionar(0, 20)
exibirEstoque()