"""
    Módulo notafiscal -
    Classe NotaFiscal - 
        Atributos :
            id        - informado.
            codigo    - informado.
            data      - informado.
            cliente   - informado.
            items     - informado
            valornota - calculado. 
"""
import datetime
from cliente        import Cliente
from produto        import Produto
from itemnotafiscal import ItemNotaFiscal

class NotaFiscal():         
    def __init__(self, Id, codigo, cliente):
        self._Id = Id
        self._codigo=codigo
        self._cliente=cliente 
        self._data=datetime.datetime.now()   
        self._itens=[]
        self._valorNota=0.0        
        
    def setCliente(self, cliente):
        if isinstance(cliente, Cliente):
            self._cliente=cliente    
            
    def adicionarItem(self, item): 
        if isinstance(item, ItemNotaFiscal):
            self._itens.append(item)
        
    def calcularNotaFiscal(self):
        valor=0.0
        for item in self._itens:
            valor = valor + item._valorItem
        self.valorNota=valor

    def imprimirNotaFiscal(self):
        ## Percorrer a coleção de itens
        ## mostrar o valor total 
        print('\n-----------------------------------------------------------------------------------')
        print('NOTA FISCAl\t\t\t\t\t\t\t     ',self._data.day,'/',self._data.month,'/',self._data.year)
        print('Cliente: ', self._cliente._codigo,'  ', 'Nome:', self._cliente._nome)
        print('CPF/CNPJ:', self._cliente._cnpjcpf)
        print('-----------------------------------------------------------------------------------')

        print('ITENS')
        print('-----------------------------------------------------------------------------------')
        print('Seq    ','Descrição                        ','QTD    ','Valor Unit          ','Preço')
        print('----  ','-------------------------------- ','-----  ','------------  ','-------------------')
        
        for item in self._itens:
            print('\n',item._sequencial, '    ', item._descricao, '   \t\t  ', item._quantidade, '\t\t', item._valorUnitario, '  \t\t     ', item._valorItem)

        print('___________________________________________________________________________________')
        print('Valor Total:', self.valorNota,'\n')       