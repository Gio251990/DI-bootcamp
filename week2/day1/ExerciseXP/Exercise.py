class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

cat1 = Cat("Buffy", 1)
cat2 = Cat("Spike", 2)
cat3 = Cat("Angel", 3)

def find_oldest_cat(cat1, cat2, cat3):
    oldest = cat1
    if cat2.age > oldest.age:
        oldest = cat2
    if cat3.age > oldest.age:
        oldest = cat3
    return oldest

oldest_cat = find_oldest_cat(cat1, cat2, cat3)
print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")






class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height
    
    def bark(self):
        print(f"{self.name} goes wolf!")

    def jump(self):
        x = self.height*2
        print(f"{self.name} jumps {x} cm high!")

dog1 = Dog("Flash", 15)
dog2 = Dog("Spike", 20)

dog1.bark()
dog2.bark()

dog1.jump()
dog2.jump()
    
if dog1.height > dog2.height:
    print(f"{dog1.name} is bigger")
else:
    print(f"{dog2.name} is bigger")





class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):  
        print("".join(self.lyrics))

stairway = Song([f"There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])
    
stairway.sing_me_a_song()





class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal in self.animals:
            print(f"{new_animal} is already inside the zoo")
        else:
            self.animals.append(new_animal)
            print(f"{new_animal} was added to the zoo")


    def get_animals(self):
        if not self.animals:
            print(f"The {self.zoo_name} has no animals")
        else:
            print(", ".join(self.animals))

    def sell_animal(self, animal_sold):
        if animal_sold not in self.animals:
            print("Animal is not inside the zoo")
        else:
            self.animals.remove(animal_sold)
            print(f"{animal_sold} was sold from the zoo")

    def sort_animals(self):
        self.animals.sort()

    def get_groups(self):
        pass

my_zoo = Zoo("Brooklyn Safari")
print(my_zoo.zoo_name)
my_zoo.add_animal("Lion")
my_zoo.add_animal("Bear")
my_zoo.add_animal("Lion")
my_zoo.add_animal("Baboon")
my_zoo.get_animals()
my_zoo.sell_animal("Bear")
my_zoo.get_animals()
my_zoo.sort_animals()
my_zoo.get_groups()

# Exercise review

class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []

    def add_animal(self, *new_animal): # usiamo *args per specificare che new_animal puo avere uno o piu animali 
        if new_animal:
            for each_animal in new_animal:
                if each_animal not in self.animals:
                    self.animals.append(each_animal)
                else:
                    print(f"{each_animal} already exist in the zoo")
    print(", "join(self.animals))
