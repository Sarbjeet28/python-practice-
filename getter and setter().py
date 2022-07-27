class test:
    def __init__(self, age = 0):
         self._age = age
      
    # getter method
    def get_age(self):
        return self._age
      
    # setter method
    def set_age(self, x):
        self._age = x
  
ob = test()
  
# setting the age using setter
ob.set_age(21)
  
# retrieving age using getter
print(ob.get_age())
print(ob._age)
