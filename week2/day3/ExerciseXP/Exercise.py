class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount



    
from func import add_number

add_number(5, 10)





import string
import random

letters = string.ascii_lowercase + string.ascii_uppercase

random_string = ""

for i in range(5):
    random_string += random.choice(letters)

print(random_string)





from datetime import datetime

current_date = datetime.now().date()
print(current_date)




current_date_time = datetime.today()
next_year = datetime(2026, 1, 1)
difference_time = next_year - current_date_time

print(difference_time)




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