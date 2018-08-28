class A():
    def __init__(self,a,b):
        self.a = int(a)
        self.b = int(b)

    def add(self):
        return self.a + self.b


#class B(A):
#    def sub(self):
#        return self.a-self.b
#count = A("3",4)
#print(count.add())
#print(B(4,5).add())
#