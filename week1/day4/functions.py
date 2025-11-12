# What is a function in Python

# - A sequence of commands that can be reused
#


# Synthax of a function:

#def <name_of_function>(empty/<argument>):
#    an indented block of code

def greetings():
    print("Welcome, user!")   # quando si fa run con questa funzione non succede nulla

greetings()

# Arguments in functions

def greetings(user_name):
    print(f"Welcome, {user_name}!") 

greetings("Gandalf")

# Default arguments

def greetings(user_name = "John"):
    print(f"Welcome, {user_name}!") 

greetings("Frodo")

# Positional arguments = the position that you enter the argument

def greetings(user_name, language):
    
    if language == "PT":
        print(f"Bem-vendo, {user_name}!")
    elif language == "IT":
        print(f"Benvenuto, {user_name}!")
    elif language == "RU":
        print(f"Privet, {user_name}")
    else:
        print(f"Welcome, {user_name}!")

greetings("Aragorn", "IT")

# create a function called country_info that receives a country name as argument
# and prints the capital of that country. Make the country name argument default
# Naboo (star wars planet). Its capital is Theed

def country(country_name = "Naboo"):

    if country_name == "Italy":
        print("Rome")
    elif country_name == "USA":
        print("Theed")
    elif country_name == "Brazil":
        print("Braziia")
    elif country_name == "Naboo":
        print("Theed")

country("Italy")

# Using the return keyword

def country(country_name = "Naboo"):

    if country_name == "Italy":
        capital = "Rome"
    elif country_name == "USA":
        capital = "Theed"
    elif country_name == "Brazil":
        capital = "Braziia"
    elif country_name == "Naboo":
        capital = "Theed"

    return capital

print(country("Italy"))


def sum_number(x, y):
    result = x + y
    return result

def multiply(j):
    multipler = sum_number(3, 2)
    result = j * multipler
    return result

print(multiply(4))