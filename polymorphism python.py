class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
    def info(self):
        print("I am a cat. My name is ", self.name)
        print("I am ", self.age ,"years old.")
 
    def make_sound(self):
        print("Meow")
 
 
class Cow:
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
    def info(self):
        print("I am a cow. My name is ", self.name)
        print("I am ", self.age ,"years old.")

    def make_sound(self):
        print("Moo")

cat1 = Cat("cattie", 3)
cow1 = Cow("Sweetie", 5)
 
for animal in (cat1, cow1):
    animal.make_sound()
    animal.info()
    animal.make_sound()
