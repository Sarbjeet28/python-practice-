class Employee():
    def __init__(self, idn, name, Add):
        self.idn = idn
        self.name = name
        self.Add = Add
 

class client(Employee):
    def __init__(self, idn, name, Add, Emails):
        super().__init__(idn, name, Add)
        self.Emails = Emails
 
Emp_1 = client(2104230, "Sarbjeet", "Ludhiana" , "sss@gmail.com")
print('The ID is:', Emp_1.idn)
print('The Name is:', Emp_1.name)
print('The Address is:', Emp_1.Add)
print('The Emails is:', Emp_1.Emails)
