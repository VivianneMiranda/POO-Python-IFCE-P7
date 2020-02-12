class Complex:
    def __init__(self):
        self.r = 0.0
        self.i = 0.0
    
    def set_i(self,i):
        self.i = i
    
    def get_i(self):
        return self.i
    
    def set_r(self,r):
        self.r = r
    
    def get_r(self):     
        return self.r
    

x = Complex()
x.set_r(3.0)
x.set_i(-2.0)

print(x.r, x.i)


    
