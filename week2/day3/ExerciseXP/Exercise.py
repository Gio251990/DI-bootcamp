class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        if self.amount == 1:
            return f"{self.amount} {self.currency}"
        else:
            return f"{self.amount} {self.currency}s"
        
    def __int__(self):
        return int(self.amount)
    
    def __repr__(self):
        if self.amount == 1:
            return f"{self.amount} {self.currency}"
        else:
            return f"{self.amount} {self.currency}s"
        
    def __add__(self, amount):
        return self.amount + amount
    
    def __add__(self, other):
        if type(other) != int and self.currency == other.currency:
            return self.amount + other.amount
        elif type(other) == int:
            return self.amount + other
        else:
            raise TypeError(f"Cannot add between Currency type {self.currency} and {other.currency}")
        
    def __iadd__(self, other):
        if type(other) != int:
            result = self.amount + int(other.amount)
            self.amount = result
            return self
        else:
            result = self.amount + other
            self.amount = result
            return self
        
    
        

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

#the comment is the expected output
print(c1)
# '5 dollars'

print(int(c1))
# 5

print(repr(c1))
# '5 dollars'

print(c1 + 5)
# 10

print(c1 + c2)
# 15

c1 += 5
print(c1)
# 10 dollars

c1 += c2
print(c1)
# 20 dollars

print(c1 + c3)
# TypeError: Cannot add between Currency type <dollar> and <shekel>








import string
import random

letters = string.ascii_lowercase + string.ascii_uppercase

random_string = ""

for i in range(5):
    random_string += random.choice(letters)

print(random_string)





import datetime

def show_date():
    current_date = datetime.date.today()
    print(current_date)

show_date()

def remaining_time():
    now = datetime.datetime.now()

    next_year = datetime.datetime(now.year + 1, 1, 1)

    difference = next_year - now
    print(difference)

remaining_time()

def time_lived(birthdate_str):

    birthdate = datetime.datetime.strptime(birthdate_str, "%Y-%m-%d")
    now = datetime.datetime.now()
    difference = now - birthdate

    minutes = difference.total_seconds() / 60
    print(f"You lived for {int(minutes)} minutes")

time_lived("1990-9-25")





from faker import Faker

users = []

def add_user(number_of_user):
    fake = Faker()
    for _ in range(number_of_user):
        user = {
            "name" : fake.name(),
            "address" : fake.address(),
            "language_code" : fake.language_code()
        }
        users.append(user)
    
add_user(5)
print(users)