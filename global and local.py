a= 19
def f1():
    global a
    b=10
    print("the value of a is",a)
    print("the value of b is" ,b)

f1()
print("the value of a is" ,a)
