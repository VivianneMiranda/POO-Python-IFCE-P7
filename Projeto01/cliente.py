from tipocliente import TipoCliente
class Cliente():
    
    def __init__(self,ide,nome,codigo,cnpjcpf,tipo): 
        self._id = id
        self._nome = nome 
        self._codigo = codigo 
        self._cnpjcpf = cnpjcpf
        self._tipo = tipo
    
    def str(self):
        string = ("ID: {0}","Nome: {1}","Codigo: {2}","Cnpj/CPF: {3}","Tipo: {4}").format(self._id,self._nome,self._codigo,self._cnpjcpf,self._tipo)
        return string
    
    if __name__ == ' __main__':
        cliente = Cliente(1,"Ana", 102 ,147 ,1)
        
       
   
    