# Decorators

import re
import datetime

class Person:
    def __init__(self, first_name, last_name, birth_date):
        self.first_name = self.format_name(first_name)
        self.last_name = self.format_name(last_name)
        self.birth_date = birth_date
        self._full_name = None # protected attribute ( _ prima dell'attributo)
        self.__salary = 36000 # private attribute ( __ prima dell'attributo)
     
    @staticmethod # a method without self - usually used for internal formating
    def format_name(name):
        name = name.strip().capitalize()
        name = re.sub(r"[^a-zA-Z]", "", name)
        return name
    

    @classmethod 
    def from_age(cls, first_name, last_name, age):
        current_year = datetime.datetime.today().year
        birth_year = current_year - age
        birth_date = f"1-1-{birth_year}"
        return Person(first_name, last_name, birth_date)  
    
    @property
    def full_name(self):
        self._full_name = f"{self.first_name} {self.last_name}"
        return self._full_name

    @full_name.setter
    def full_name(self):
        self._full_name = f"{self.first_name} {self.last_name}"

    def presentation(self):
        print(f"Hello, my name is {self.full_name}")

    # Dunder method:

    def __str__(self):
        return f"Hello, my name is {self.full_name}, my birthdate is {self.birth_date}"
    
    def __repr__(self):
        return f"{self.__dict__}"
    
    def __eq__(self, other):
        return len(self.first_name) == len(other.first_name)



person1 = Person("John", "Snow", "05-12-1980")
person2 = Person("ARIA", "STARK", "30-07-2000")

print(person1.first_name)
print(person2.first_name)

print(person1)

print(datetime.datetime.today().year)

# Creating an object using in our class method

person3 = Person.from_age("Sansa", "Stark", 30)
print(person3.birth_date)
print(person1 == person2)

# Create a static method that format the first_name and last_name as full_name than 
# create an internal attribute called full_name and do it with the static method
# create person4 name: Daenarys Targaryen age: 32
# print Daenarys full_name

person4 = Person("Daenarys", "Targaryen", 32)
print(person4.full_name)
# print(person4.__salary) # the traditional way give us an error, but there is a special way that we can access a private attribute:
print(person2._Person__salary) # the not traditional way of 
person2.presentation()