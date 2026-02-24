import tkinter as tk
from tkinter import messagebox
import mysql.connector

conexao = mysql.connector.connect(
            host='localhost',
            user='murilo',
            password='0000',
            database='loja',
        )
cursor = conexao.cursor()

def cadastrarProduto():
    def enviar():
        conexao = mysql.connector.connect(  
            host='localhost',
            user='murilo',
            password='0000',
            database='loja',
        )
        cursor = conexao.cursor()
        id_produto = float(entry_id.get())
        nome = entry_nome.get()
        valor = float(entry_valor.get())
        
        comando = f'INSERT INTO vendas(nome, valor, id_produto) VALUES("{nome}", {valor}, {id_produto});'
        cursor.execute(comando)
        conexao.commit()
        cursor.close()
        conexao.close()
        messagebox.showinfo("Cadastro", "Produto cadastrado com sucesso!")
        janela.destroy()

    def cancelar():
        janela.destroy()

    janela = tk.Toplevel()
    janela.title("Cadastrar Produto")
    janela.geometry("500x500")

    tk.Label(janela, text="ID do Produto:").pack() 
    
    entry_id = tk.Entry(janela)
    entry_id.pack()

    tk.Label(janela, text="Nome do Produto:").pack()
    entry_nome = tk.Entry(janela)
    entry_nome.pack()

    tk.Label(janela, text="Valor do Produto:").pack()
    entry_valor = tk.Entry(janela)
    entry_valor.pack()

    tk.Button(janela, text="Cadastrar", command=enviar).pack(pady=10)
    tk.Button(janela, text="Cancelar", command=cancelar).pack(pady=5)

def pesquisarProduto():
    def buscar():
        conexao = mysql.connector.connect(
            host='localhost',
            user='murilo',
            password='0000',
            database='loja',
        )
        cursor = conexao.cursor()
      
        id_produto = float(entry_id.get())
        cursor = conexao.cursor()
        comando = f'SELECT nome, valor FROM vendas WHERE id_produto = {id_produto};'
        cursor.execute(comando)
        resultado = cursor.fetchall()
        resultado_text.delete("1.0", tk.END)
        for linha in resultado:
            resultado_text.insert(tk.END, f"Nome: {linha[0]}, Valor: {linha[1]}\n")
        cursor.close()
        conexao.close()

    janela = tk.Toplevel()
    janela.title("Pesquisar Produto")
    janela.geometry("500x500")

    tk.Label(janela, text="ID do Produto:").pack()
    entry_id = tk.Entry(janela)
    entry_id.pack()

    tk.Button(janela, text="Pesquisar", command=buscar).pack(pady=5)

    resultado_text = tk.Text(janela, height=5, width=40)
    resultado_text.pack()

def atualizarProduto():
    def atualizar():
        conexao = mysql.connector.connect(
            host='localhost',
            user='murilo',
            password='0000',
            database='loja',
        )
        cursor = conexao.cursor()
        id_produto = int(entry_id.get())
        opcao = int(entry_opcao.get())
        cursor = conexao.cursor()

        if opcao == 1 or opcao == 3:
            novo_nome = entry_nome.get()
            comando = f'UPDATE vendas SET nome = "{novo_nome}" WHERE id_produto = {id_produto};'
            cursor.execute(comando)
            conexao.commit()

        if opcao == 2 or opcao == 3:
            novo_valor = float(entry_valor.get())
            comando = f'UPDATE vendas SET valor = "{novo_valor}" WHERE id_produto = {id_produto};'
            cursor.execute(comando)
            conexao.commit()

        cursor.close()
        conexao.close()
        messagebox.showinfo("Atualização", "Produto atualizado com sucesso!")
        janela.destroy()

    janela = tk.Toplevel()
    janela.title("Atualizar Produto")
    janela.geometry("500x500")

    tk.Label(janela, text="ID do Produto:").pack()
    entry_id = tk.Entry(janela)
    entry_id.pack()

    tk.Label(janela, text="Opção (1=Nome, 2=Preço, 3=Ambos):").pack()
    entry_opcao = tk.Entry(janela)
    entry_opcao.pack()

    tk.Label(janela, text="Novo Nome (se aplicável):").pack()
    entry_nome = tk.Entry(janela)
    entry_nome.pack()

    tk.Label(janela, text="Novo Valor (se aplicável):").pack()
    entry_valor = tk.Entry(janela)
    entry_valor.pack()

    tk.Button(janela, text="Atualizar", command=atualizar).pack(pady=10)

def apagarProduto():
    def deletar():

        conexao = mysql.connector.connect(
            host='localhost',
            user='murilo',
            password='0000',
            database='loja',
        )
        cursor = conexao.cursor()
        
        id_produto = int(entry_id.get())
        cursor = conexao.cursor()
        comando = f'DELETE FROM vendas WHERE id_produto = {id_produto}'
        cursor.execute(comando)
        conexao.commit()
        cursor.close()
        conexao.close()
        messagebox.showinfo("Deletar", "Produto deletado com sucesso!")
        janela.destroy()

    janela = tk.Toplevel()
    janela.title("Deletar Produto")
    janela.geometry("500x500")

    tk.Label(janela, text="ID do Produto para deletar:").pack()
    entry_id = tk.Entry(janela)
    entry_id.pack()

    tk.Button(janela, text="Deletar", command=deletar).pack(pady=10)


root = tk.Tk()
root.title("Sistema de Vendas")
root.geometry("300x300")

tk.Label(root, text="Menu de Opções", font=("Arial", 14)).pack(pady=20)

tk.Button(root, text="Cadastrar Produto", width=25, command=cadastrarProduto).pack(pady=5)
tk.Button(root, text="Pesquisar Produto", width=25, command=pesquisarProduto).pack(pady=5)
tk.Button(root, text="Atualizar Produto", width=25, command=atualizarProduto).pack(pady=5)
tk.Button(root, text="Deletar Produto", width=25, command=apagarProduto).pack(pady=5)

root.mainloop()
