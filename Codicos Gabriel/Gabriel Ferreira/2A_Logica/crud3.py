import os
import mysql.connector
os.system('clear || cls')
conexao = mysql.connector.connect(
  host='localhost',
  user='murilo',
  password='0000',
  database='loja',
)
cursor = conexao.cursor()
#Create
def cadastrarProduto():
  id_produto = float(input('Qual o id do produto? '))
  nome = str(input('Qual o nome do produto? '))
  valor = float(input('Qual o valor do produto? '))
  comando = f'insert into vendas(nome, valor, id_produto) values("{nome}", {valor}, {id_produto});'
  cursor.execute(comando)
  conexao.commit()
  cursor.close()
  conexao.close()
#Read
def pesquisarProduto():
  id_produto = float(input('Qual o id do produto? '))
  comando = f'select nome, valor from vendas where id_produto = {id_produto};'
  cursor.execute(comando)
  resultado = cursor.fetchall() 
  print(resultado)
  cursor.close()
  conexao.close()
#Update 
def atualizarProduto():
  id_produto = int(input('Digite o id do produto que você deseja atualizar?:'))
  opcao = int(input('Digite a opção desejada:\n1) Atualizar o nome\n2) Atualizar o preço\n3) Atualizar nome e preço\n'))
  if(opcao == 1) or (opcao == 3):
    novo_nome = str(input(f'Qual será o novo nome do produto de código {id_produto} '))
    comando = f'update vendas set nome = "{novo_nome}" where id_produto  = {id_produto};'
    cursor.execute(comando)
    conexao.commit()
  if(opcao == 2) or (opcao == 3):
      novo_valor=float(input(f'Digite o valor do novo produto de código {id_produto}: '))
      comando = f'update vendas set valor= "{novo_valor}" where id_produto = {id_produto};'
      cursor.execute(comando)
      conexao.commit()
  cursor.close()
  conexao.close()

def apagarProduto():
  id_produto = int(input('Qual o código id do produto que você quer deletar?'))
  comando = f'delete from vendas where id_produto = {id_produto}'
  print('Dados sendo mandados para atualização')

op = int(input('Digite a opção desejada:\n1) Cadastrar um produto\n2) Pesquisar um produto\n3) Atualizar um produto\n4) Deletar um produto\n'))
if(op == 1):
  cadastrarProduto()
elif(op == 2):
  pesquisarProduto()
elif(op == 3):
  atualizarProduto()
elif(op == 4):
  apagarProduto()
else:
  print('Opção inválida')