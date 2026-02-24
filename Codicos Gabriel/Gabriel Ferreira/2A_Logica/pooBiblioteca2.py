class Livro:
  def __init__ (self, titulo, autor, ano, livros):  
    self.titulo = titulo
    self.autor = autor
    self.ano = ano
    self.livros = []
  def adicionarLivro(self, nome):
    self.livros.append(nome)
  