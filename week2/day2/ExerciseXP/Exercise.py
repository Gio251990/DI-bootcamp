class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'
    
class Siamese(Cat):
    pass

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'
    
bengal_obj = Bengal("BengalCat", 2)
chartreux_obj = Chartreux("ChartreuxCat", 4)
siamese_obj = Siamese("SiameseCat", 3)
    
all_cats = [bengal_obj, chartreux_obj, siamese_obj]

sara_pets = Pets(all_cats)

sara_pets.walk()





class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return(f"{self.name} is barking")

    def run_speed(self):
        result = self.weight/self.age*10
        return(result)

    def fight(self, other_dog):
        result_self = self.run_speed() * self.weight
        result_other_dog = other_dog.run_speed() * other_dog.weight
        if result_self > result_other_dog:
            return(f"{self.name} won the fight, against {other_dog.name}")
        elif result_self < result_other_dog:
            return(f"{other_dog.name} won the fight, against {self.name}")
        else:
            return f"The fight between {self.name} and {other_dog.name} is a tie"

dog1 = Dog("Rex", 5, 20)
dog2 = Dog("Max", 2, 8)
dog3 = Dog("Jack", 9, 26)

dogs = [dog1, dog2, dog3]

print(dog2.bark())
print(dog1.run_speed())
print(dog1.fight(dog2))
print(dog2.fight(dog3))
print(dog3.fight(dog1))



class Person:
    def __init__(self, first_name, age):
        self.first_name = first_name
        self.age = age
        self.last_name = ""

    def is_18(self):
        return self.age >= 18
    
class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []

    def born(self, first_name, age):
        new_person = Person(first_name, age)
        new_person.last_name = self.last_name
        self.members.append(new_person)

    def check_majority(self, first_name):
        for person in self.members:
            if person.first_name == first_name:
                if person.is_18():
                    print("You are over 18, your parents Jane and John accept that you will go out with your friends")
                else:
                    print("Sorry, you are not allowed to go out with your friends.")
                return
            print("Person not found in the family")

    def family_presentation(self):
        print(f"Family: {self.last_name}")
        for member in self.members:
            print(f"{member.first_name}, {member.age} years old")

my_family = Family("Spizzichino")
my_family.born("Giovanni", 35)
my_family.born("Arielle", 4)

my_family.family_presentation()

my_family.check_majority("Giovanni")
my_family.check_majority("Arielle")




