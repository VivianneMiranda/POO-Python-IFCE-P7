class Produto():
    def __init__(self, id, codigo, desc, valor):
        self.id = id
        self.codigo = codigo
        self.desc = desc
        self.valor = valor
        
    def str(self):
        string = "Id = {3} Código = {2} Descrição = {1} Valor = {0}".format (self.valor,self.desc,self.codigo,self.id)
        return string    
    
    