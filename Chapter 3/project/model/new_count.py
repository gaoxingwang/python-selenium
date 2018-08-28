from count import A

class C(A):
    def mul(self):
        return self.a * self.b

C = C(1,2)
print(C.mul())
