from produto import Produtos
from tkinter import *

class Application:
    def __init__(self, master=None):
        self.fonte = ("Verdana", "8")

        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()
        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()
        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3["pady"] = 10
        self.container3.pack()
        self.container4 = Frame(master)
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()
        self.container5 = Frame(master)
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.pack()
        self.container6 = Frame(master)
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.pack()
        self.container7 = Frame(master)
        self.container7["padx"] = 20
        self.container7["pady"] = 5
        self.container7.pack()
        self.container8 = Frame(master)
        self.container8["padx"] = 20
        self.container8["pady"] = 10
        self.container8.pack()
        self.container9 = Frame(master)
        self.container9["pady"] = 15
        self.container9.pack()

        self.titulo = Label(self.container1, text="Informe os dados do produto:")
        self.titulo["font"] = ("Calibri", "9", "bold")
        self.titulo.pack ()

        self.lblidProduto = Label(self.container2,
        text="idProduto:", font=self.fonte, width=10)
        self.lblidProduto.pack(side=LEFT)

        self.txtidProduto = Entry(self.container2)
        self.txtidProduto["width"] = 10
        self.txtidProduto["font"] = self.fonte
        self.txtidProduto.pack(side=LEFT)

        self.btnBuscar = Button(self.container2, text="Buscar",
        font=self.fonte, width=10)
        self.btnBuscar["command"] = self.buscarProduto
        self.btnBuscar.pack(side=RIGHT)

        self.lblproduto = Label(self.container3, text="Produto:",
        font=self.fonte, width=23)
        self.lblproduto.pack(side=LEFT)

        self.txtproduto = Entry(self.container3)
        self.txtproduto["width"] = 25
        self.txtproduto["font"] = self.fonte
        self.txtproduto.pack(side=LEFT)

        self.lblprecoc = Label(self.container4, text="Preço de Compra:",
        font=self.fonte, width=23)
        self.lblprecoc.pack(side=LEFT)

        self.txtprecoc = Entry(self.container4)
        self.txtprecoc["width"] = 25
        self.txtprecoc["font"] = self.fonte
        self.txtprecoc.pack(side=LEFT)

        self.lblprecov= Label(self.container5, text="Preço de Venda:",
        font=self.fonte, width=23)
        self.lblprecov.pack(side=LEFT)

        self.txtprecov = Entry(self.container5)
        self.txtprecov["width"] = 25
        self.txtprecov["font"] = self.fonte
        self.txtprecov.pack(side=LEFT)

        self.lblqtdestoque= Label(self.container6, text="Quantidade do estoque:",
        font=self.fonte, width=23)
        self.lblqtdestoque.pack(side=LEFT)

        self.txtqtdestoque = Entry(self.container6)
        self.txtqtdestoque["width"] = 25
        self.txtqtdestoque["font"] = self.fonte
        self.txtqtdestoque.pack(side=LEFT)

        self.lblfornecedor= Label(self.container7, text=" Fornecedor:",
        font=self.fonte, width=23)
        self.lblfornecedor.pack(side=LEFT)

        self.txtfornecedor = Entry(self.container7)
        self.txtfornecedor["width"] = 25
        self.txtfornecedor["font"] = self.fonte
        self.txtfornecedor.pack(side=LEFT)

        self.bntInsert = Button(self.container8, text="Inserir",font=self.fonte, width=12)
        self.bntInsert["command"] = self.inserirProduto
        self.bntInsert.pack (side=LEFT)

        self.bntAlterar = Button(self.container8, text="Alterar",font=self.fonte,width=12)
        self.bntAlterar["command"] = self.alterarProduto
        self.bntAlterar.pack (side=LEFT)

        self.bntExcluir = Button(self.container8, text="Excluir",font=self.fonte,bg='red', width=12)
        self.bntExcluir["command"] = self.excluirProduto
        self.bntExcluir.pack(side=LEFT)

        self.lblmsg = Label(self.container9, text="")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()


    def inserirProduto(self):
        user = Produtos()

        user.produto = self.txtproduto.get()
        user.precoc = self.txtprecoc.get()
        user.precov = self.txtprecov.get()
        user.qtdestoque = self.txtqtdestoque.get()
        user.fornecedor= self.txtfornecedor.get()

        self.lblmsg["text"] = user.insertUser()

        self.txtidProduto.delete(0, END)
        self.txtproduto.delete(0, END)
        self.txtprecoc.delete(0, END)
        self.txtprecov.delete(0, END)
        self.txtqtdestoque.delete(0, END)
        self.txtfornecedor.delete(0, END)



    def alterarProduto(self):
        user = Produtos()

        user.produto = self.txtproduto.get()
        user.precoc = self.txtprecoc.get()
        user.precov = self.txtprecov.get()
        user.qtdestoque = self.txtqtdestoque.get()
        user.fornecedor= self.txtfornecedor.get()
    
        self.lblmsg["text"] = user.updateUser()

        self.txtidProduto.delete(0, END)
        self.txtproduto.delete(0, END)
        self.txtprecoc.delete(0, END)
        self.txtprecov.delete(0, END)
        self.txtqtdestoque.delete(0, END)
        self.txtfornecedor.delete(0, END)




    def excluirProduto(self):
        user = Produtos()

        user.idProduto = self.txtidProduto.get()

        self.lblmsg["text"] = user.deleteUser()

        self.txtidProduto.delete(0, END)
        self.txtproduto.delete(0, END)
        self.txtprecoc.delete(0, END)
        self.txtprecov.delete(0, END)
        self.txtqtdestoque.delete(0, END)
        self.txtfornecedor.delete(0, END)


    def buscarProduto(self):
        user = Produtos()

        idProduto = self.txtidProduto.get()

        self.lblmsg["text"] = user.selectUser(idProduto)

        self.txtidProduto.delete(0, END)
        self.txtidProduto.insert(INSERT, user.idProduto)

        self.txtproduto.delete(0, END)
        self.txtproduto.insert(INSERT, user.produto)

        self.txtprecoc.delete(0, END)
        self.txtprecoc.insert(INSERT,user.precoc)

        self.txtprecov.delete(0, END)
        self.txtprecov.insert(INSERT, user.precov)

        self.txtqtdestoque.delete(0, END)
        self.txtqtdestoque.insert(INSERT, user.qtdestoque)

        self.txtfornecedor.delete(0, END)
        self.txtfornecedor.insert(INSERT,user.fornecedor)


root = Tk()
Application(root)
root.mainloop()