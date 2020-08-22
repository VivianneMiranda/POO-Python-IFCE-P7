#importando módulo do SQlite
import sqlite3

class Banco():
    def __init__(self):
        self.conexao = sqlite3.connect('banco.db')
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()

        c.execute("""create table if not exists produtos (
                    idProduto integer primary key autoincrement ,
                    produto text,
                    precoc text,
                    precov text,
                    qtdestoque text,
                    fornecedor text)""")
        self.conexao.commit()
        c.close()
