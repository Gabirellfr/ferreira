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
# # CREATE
# id_produto = int(input('Qual o id do produto?'))
# nome = str(input('Qual o nome do produto?'))
# valor = int(input('Qual o valor do produto?'))
# comando = f'INSERT INTO vendas (id_produto, nome, valor) VALUES ({id_produto},"{nome}", {valor})' #comando sql pra adicionar valores
# cursor.execute(comando) #executa o comando
# conexao.commit() # salva a informação no banco de dados
# cursor.close()
# conexao.close()

# READ PESQUISAR
id_produto = int(input('Qual o id do produto que você deseja pesquisar?'))
comando = f'select nome, valor from vendas where id_produto = {id_produto}' #comando sql para consultar algum produto
cursor.execute(comando)
resultado = cursor.fetchall() # ler o banco de dados
print(resultado)
cursor.close()
conexao.close()

#UPDATE ATUALIZAR
# id_produto = int(input('Qual o código id do produto que você quer fazer uma alteração?'))
# escolha = int(input('Digite qual opção retrata os valores que você deseja alterar:\n1) Alterar o nome do Produto\n2) Alterar o valor do Produto\n3) Alterar nome e valor do Produto\n'))
# if ((escolha == 2) or (escolha == 3)):
#   novo_valor = int(input(f'Qual o novo valor do produto de código {id_produto}?'))
#   comando = f'UPDATE vendas SET valor = {novo_valor} WHERE id_produto = {id_produto}'
#   print('Dados sendo mandados para atualização')
# elif ((escolha == 1) or (escolha == 3)):
#   nome_produto = str(input(f'Qual o novo nome do produto de código {id_produto}?'))
#   comando = f'UPDATE vendas SET nome = "{nome_produto}" WHERE id_produto = {id_produto}'
#   print('Dados sendo mandados para atualização')
# else:
#   print('Seu animal, essa opção não existe')
# cursor.execute(comando) #executa o comando
# conexao.commit() # salva a informação no banco de dados
# cursor.close()
# conexao.close()

#DELETE APAGAR
# id_produto = int(input('Qual o código id do produto que você quer deletar?'))
# comando = f'delete from vendas where id_produto = {id_produto}'
# print('Dados sendo mandados para atualização')

# cursor.execute(comando) #executa o comando
# conexao.commit() # salva a informação no banco de dados
# cursor.close()
# conexao.close()
