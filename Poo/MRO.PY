class A: 
    def hablar (self):
        print("Hola desde A")
class B(A): 
    def hablar (self):
        print("Hola desde B")
class C(A): 
    def hablar (self):
        print("Hola desde C")
class D(B, C): 
    def hablar (self):
        print("Hola desde D")

d = D()
#D>B>C>A
d.hablar()
#print(D.mro())
d2 = D()

B.hablar(d2)