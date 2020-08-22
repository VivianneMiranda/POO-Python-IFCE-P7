from bd import Banco

class Produtos(object):
    def __init__(self, idProduto = 0, produto= "", precoc = "",precov = "", qtdestoque = "", fornecedor = ""):
        self.info = {}
        self.idProduto = idProduto
        self.produto = produto
        self.precoc = precoc
        self.precov = precov
        self.qtdestoque = qtdestoque
        self.fornecedor = fornecedor


    def insertUser(self):
        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("insert into produtos (produto,  precoc, precov,qtdestoque, fornecedor) values ('" + self.produto + "', '" +self.precoc + "', '" + self.precov + "', '" +self.qtdestoque + "', '" + self.fornecedor + "' )")

            banco.conexao.commit()
            c.close()

            return "Produto cadastrado com sucesso!"
        except:
            return "Ocorreu um erro na inserção do produto"

    def updateUser(self):
        
        banco = Banco()
        try:

            c = banco.conexao.cursor()
            
            c.execute("update produtos set produto = '" + self.produto + "', precoc = '" + self.precoc + "', precov = '" + self.precov + "', qtdestoque = '" + self.qtdestoque + "', fornecedor = '" + self.fornecedor + "' where idProduto = " + self.idProduto + " ")
            
            banco.conexao.commit()
            c.close()

            return "Produto atualizado com sucesso!"
        except:
            return "Ocorreu um erro na alteração do produto"

    def deleteUser(self):
        
        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("delete from produtos where idProduto = " + self.idProduto + " ")

            banco.conexao.commit()
            c.close()

            return "Produto excluído com sucesso!"
        except:
            return "Ocorreu um erro na exclusão do produto"

    def selectUser(self, idProduto):
        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("select * from produtos where idProduto = " + idProduto + "  ")

            for linha in c:
                self.idProduto = linha[0]
                self.produto = linha[1]
                self.precoc = linha[2]
                self.precov = linha[3]
                self.qtdestoque = linha[4]
                self.fornecedor = linha[5]

                c.close()

                return "Busca feita com sucesso!"
        except:
                return "Ocorreu um erro na busca do produto"