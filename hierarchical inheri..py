class A:
    def __init__(self):
        print('***Take inputs from user and diplay the sum of two numbers***')
    
    def f1(self):
        a=int(input('Enter the value of a: '))
        b=int(input('Enter the value of b: '))
        print(a+b)

class B(A):
    def f2(self):
        c=int(input('Enter the value of c: '))
        d=int(input('Enter the value of d: '))
        print(c+d)
        
        

class C(A):
    def f3(self):
        e=int(input('Enter the value of e: '))
        f=int(input('Enter the value of f: '))
        print(e+f)
        

c1=C()
c1.f1()
c1.f3()
b1=B()
b1.f2()

