from threading import*
class A(thread):
    def run(self):
        for x in range(5):
            print(x)

ob=A()
ob.start()
or
ob=A()
t1=thread(target=ob.run)
t1.start
