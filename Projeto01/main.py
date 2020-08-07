"""
  Módulo main - instancia objetos de classes definidas em
                módulos do pacote projeto01.   
"""
from produto        import Produto
from cliente        import Cliente
from notafiscal     import NotaFiscal
from itemnotafiscal import ItemNotaFiscal
from tipocliente    import TipoCliente


def main():
    
    cliente=Cliente(1, "José Simão da Silva", 1234, "200.100.345-34", 1)
    #informações do cliente
    
    p1=Produto(1,100,"Arroz Agulha", 5.50) #infomarções do produto e da compra do produto
    it1=ItemNotaFiscal(1, 1, 10, p1)
    
    
    p2=Produto(2,200,"Feijao Mulatinho", 8.50)  #infomarções do produto e da compra do produto
    it2=ItemNotaFiscal(2, 2, 10, p2)
    
    p3=Produto(3,300,"Macarrao Fortaleza", 4.50)  #infomarções do produto e da compra do produto
    it3=ItemNotaFiscal(3, 3, 10, p3)
    
    nf = NotaFiscal(1,100,cliente)
    
    nf.adicionarItem(it1)
    
    nf.adicionarItem(it2)
    
    nf.adicionarItem(it3)
    
    nf.calcularNotaFiscal()
    
    nf.imprimirNotaFiscal()

if __name__ == '__main__':
    main()