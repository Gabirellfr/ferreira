import os
os.system('clear || cls')
class Livro:
  def __init__(self, titulo, autor, ano):
    self.titulo = titulo
    self.autor = autor
    self.ano = ano
    self.livros = []
  def adicionar_livro(self, livro):
    self.livros.append(livro)
  def listar_livros(self):
    for livro in self.livros:
      print(f"{livro.titulo}, {livro.autor}, {livro.ano}")
# Uso das classes
biblioteca = Livro('', '', 0)
biblioteca.adicionar_livro(Livro("1934", "George Orwell", 1949))
biblioteca.adicionar_livro(Livro("Bíblia", "Vários Autores", '1500 a.c'))
biblioteca.listar_livros()

# import os
# os.system('clear || cls')

# class Livro:
#   def __init__(self, titulo, autor, ano):
        # self.titulo = titulo
#     self.autor = autor
#     self.ano = ano

# class biblioteca:
#   def __init__(self, livros):
#     self.livros = livros[Livro]
      
#   def adicionar_livro(self, livro):
#     self.livros.append(livro)

#   def listar_livros(self):
#     for livro in self.livros:
#       print(f"{livro.titulo}, {livro.autor}, {livro.ano}")

# # Uso das classes
# biblioteca = ()
# biblioteca.adicionar_livro(Livro("1984", "George Orwell", 1949))
# biblioteca.listar_livros()