print("### CLASSES ###")

class Class1:
    x = 5
obj1 = Class1()
print(obj1.x)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name}({self.age})"
    def method1(self):
        print("Hello my name is " + self.name)

obj2 = Person("John", 36)
print(obj2.name)
print(obj2.age)
print(obj2)
obj2.method1()

obj2.age = 40
print(obj2.age)

del obj2.age
del obj2



print("## Inheritance ##")
class ClassParent:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printName(self):
        print(self.firstname, self.lastname)

class ClassChild(ClassParent):
    def __init__(self, fname, lname, age):
        super().__init__(fname, lname)
        self.age = age
    def printAge(self):
        print(self.age)

obj3 = ClassChild("Name", "Lname", 56)
obj3.printName()
obj3.printAge()



print("## Polymorphism ##")

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Move!")

class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self):
        print("Sail!")

class Plane(Vehicle):
    def move(self):
        print("Fly!")

car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object

for x in (car1, boat1, plane1):
    print(x.brand)
    print(x.model)
    x.move()
