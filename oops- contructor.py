class computer:
    def __init__(self,a,b):
        self.a= a
        self.b=b
    def config(self):
       print('config is', self.a, self.b)

x = computer('i5', 16)
y=computer('ryzan', 8)




x.config()
y.config()