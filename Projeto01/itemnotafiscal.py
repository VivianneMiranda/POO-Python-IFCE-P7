from produto import Produto

class ItemNotaFiscal():
    
    def __init__(self, id, sequencial, quantidade, produto):
        self._id=id
        self._sequencial=sequencial
        self._quantidade=quantidade
        self._produto=produto
        
        self._descricao=self._produto.getDescricao()
        self._valorUnitario=self._produto.getValorUnitario()
        self._valorItem=float(self._quantidade * self._valorUnitario)
      
    def str(self):
        string="\nId= {5}\nSequencial= {4}\nQuantidade= {3}\nProduto= {2}\nValor Unitario= {1}\nValor Item= {0}\n".format(self._valorItem,
                                                                                                             self._valorUnitario,
                                                                                                             self._descricao, 
                                                                                                             self._quantidade, 
                                                                                                             self._sequencial, 
                                                                                                             self._id)
        return string
    
        
if __name__ == '__main__':
    produto = Produto(1,100,'Arroz', 5.5) 
    item=ItemNotaFiscal(1, 1, 12, produto)
    print(item.str())
        