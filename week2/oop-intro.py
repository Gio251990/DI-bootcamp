# OOP - OBJECT ORIENTED PROGRAMING

# HOW TO CREATE A CLASS OBJECT

class Dog: # il nome della classe deve cominciare con la lettera maiuscola
    def __init__(self, name, color, breed, age, is_trained): # __init__ usato per inizializzare un oggetto di una classe (constructor function)
        self.name = name
        self.color = color
        self.breed = breed
        self.age = age
        self.is_trained = is_trained

    def bark(self): # function > method
        print(f"{self.name} goes bau bau\n"*self.age)

    def run(self):
        if self.age > 5:
            print(f"{self.name} prefers to walk")
        else:
            print(f"{self.name} is running")

    def walk(self, person):
        print(f"{person} is walking with {self.name}")

    def rename(self, new_name):
        self.name = new_name
        return self


        

# HOW TO CREATE AN OBJECT OF A SPECIFIC CLASS
dog1 = Dog("Rex", "black", "german shepherd", 8, True) # il type della stringa e' .Dog
print(dog1)

# Accessing the attributes of a dog:
print(dog1.name)
print(dog1.age)
print(dog1.is_trained)
print(dog1.__dict__) # crea uno storage per tutte le keys da poter riutilizzare

dog1.guidance_dog = True
print(dog1.guidance_dog)

# create a second obgect of class Dog, call it dog2 and you choose the attribute

dog2 = Dog("Flash", "silver", "husky" , 1, False)
print(dog2.name)
print(dog2.__dict__) # riutilizza tutte le keys di dog1.__dict__

# CALL THE METHOD

dog1.bark()
dog2.bark()

# Create a method called run() that checkes the dog's age and if the dog is older than 5 you print "dog.name" prefers to walk and you print "dog.name" is running
# then call the method on dog2

dog1.run()
dog2.run()

dog2.walk("John")
dog2.rename("Toto")
print(dog2.name)
print(dog2.__dict__)

# Create a class called BankAccount, with 3 attributes:
# account holder = name + last name of the person
# account number = random number
# balance = which is starts with 50.00 (float)

class BankAccount:
    def __init__(self, account_holder, account_number, balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

bankaccount1 = BankAccount("Giovanni", 123, float(150))
bankaccount2 = BankAccount("John", 568, float(789))
bankaccount3 = BankAccount("Nick", 897, float(7589))

print(bankaccount1.__dict__)
print(bankaccount2.__dict__)
print(bankaccount3.__dict__)

import datetime
class BankAccount:
    def __init__(self, account_holder, account_number, balance = 50.00):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance
        self.transaction = []
    
    def view_balance(self):
        report = f"""account holder: {self.account_holder}
                account number: {self.account_number}
                balance: {self.balance}"""
        print(report)

    def deposit(self, amount):
        self.transaction.append(f"{datetime.datetime.now()} --- deposit {amount}")
        if amount <= 0:
            print("Invalid amount")
        else:
            self.balance += amount
        return self.balance

    def withdrawal(self, amount):
        self.transaction.append(f"{datetime.datetime.now()} --- withdrawal {amount}")
        if amount <= 0:
            print("Invalid amount")
        elif self.balance < amount:
            print("You dont have enought money")
        else:
            self.balance -= amount
        return self.balance
    
    def view_transaction(self):
        for transaction in self.transaction:
            print(transaction)

    
bankaccount1 = BankAccount("Giovanni", 123, float(150))
bankaccount2 = BankAccount("John", 568, float(789))
bankaccount3 = BankAccount("Nick", 897, float(7589))

bankaccount1.view_balance()
bankaccount1.deposit(100)
bankaccount1.withdrawal(200)


# Create a new attribute called transaction: it is a list







        





















