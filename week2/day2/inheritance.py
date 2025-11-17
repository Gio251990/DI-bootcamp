# INHARITANCE: PASSING ATTRIBUTES OR "BEHAVIOR" FROM A "FAMILY" MEMBER TO ANOTHER

class Parent:
    def speak(self):
        print("Parent is speaking")

class Child(Parent):
    def speak(self):
        print("Child is speaking")

class Grandchild(Child):
    pass

child1 = Child()
child1.speak()

grandchild1 = Grandchild()
grandchild1.speak()

# inhariting attributes

class Animal:
    def __init__(self, name, family, legs):
        self.name = name
        self.family = family
        self.legs = legs

    def sleep(self):
        return f"{self.name} is sleeping"

class Dog(Animal):
    
    def __init__(self, name, family, legs, trained, age):
        super().__init__(name, family, legs)
        self.trained = trained
        self.age = age

dog1 = Dog("Flufy", "Canidae", 4, True, 5)
print(dog1.sleep())

# create a cat class the inherits form animal all the attributs + friendly and house_cat

class Cat(Animal):

    def __init__(self, name, family, legs, friendly, house_cat):
        super().__init__(name, family, legs)
        self.friendly = friendly
        self.house_cat = house_cat
        
cat1 = Cat("Fuffy", "Felidae", 4, False, True)
print(cat1.friendly)


# multiple inheritance

class Alien:

    def __init__(self, alien_name, planet):
        self.alien_name = alien_name
        self.planet = planet

class AlienDog(Alien, Dog): # the order metter
    def __init__(self, alien_name, planet, name, family, legs, trained, age):
        Alien.__init__(self, alien_name, planet)
        Dog.__init__(self, name, family, legs, trained, age)

aliendog1 = AlienDog("Chubi", "Mars", "Bob", "Canidae", 6, True, 10)
print(aliendog1.planet)





    
