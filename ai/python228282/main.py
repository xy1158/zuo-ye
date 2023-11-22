class Person:
    def __init__(self, name):
        self.name = name
    def getname(self):
        print(self.name)


person1 = Person("bateman")
person1.getname()
