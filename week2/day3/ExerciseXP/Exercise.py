class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount



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