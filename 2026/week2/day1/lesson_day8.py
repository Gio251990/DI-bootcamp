# FUNCTIONS

def say_hello():
    print("Hello Alice")
    print("Hello Bob")

say_hello()

def say_hello(name):
    print(f"Hi {name}")

say_hello("Bob")
say_hello("Alice")

def say_hello(username, language = "EN"): # cosi il language viene impostato come EN di default
    if language == "EN":
        print("Hello "+ username)
    elif language == "FR":
        print("Bonjour "+ username)
    else:
        print("This language is not supported: " + language)
    
say_hello("Rick", "FR") # passing by position
say_hello(username="Rick", language="FR") # passing by keywords argument
say_hello("Rick", language="FR") # mix

# GLOBAL SCOPE

name = 'Avner'

def say_hi():
  print(name)

say_hi()


# CALCULATOR

def calculator(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2

print(calculator(num1=1, num2=5, operation="+"))
print(calculator(1, 5, "*"))


def capitalize(first_name, last_name):
    return [first_name.capitalize(), last_name.capitalize()]

first_name, last_name = capitalize("bob", "something")
print(first_name, last_name)


def calculate_temperature(speed, sun_temp):
    if speed < 10 and sun_temp < 20:
        return 10, 20
    elif speed < 20 and sun_temp < 30:
        return 20, 30
    else:
        return 30, 40

low_temperature, high_temperature = calculate_temperature(5, 15)
if low_temperature > 5 and high_temperature <= 20:
    print("It's too cold")



def calculation(a, b):
    add = a + b
    sub = a - b
    return add, sub

res = calculation(40, 10)
print(res)


# PASSING A FUNCTION

def greet_users(users):             # users should be a list
    for user in users:              # Because it's a list, we can loop through it
        print("Hello " + user.title() + " !")       # For each user, print "hello" and then his name

usernames = ["steve", "stan", "debbie"]
greet_users(usernames)


# COPY

d1 = {
    "a": 1,
    "b": 2,
    "c": 3
}

d2 = d1.copy()

print(d1)
print(d2)



def my_f1():
    print("Hello")

def my_f2():
    print("Word")

def my_f3():
    print("This is Rick!")

list_of_functions = [my_f1, my_f2, my_f3]

for function in list_of_functions:
    function()


# ARGS

def my_print (*args):
    print(args)
    print(type(args))

my_print("5", 1, True)

# KWARGS

def my_print (**kwargs):
    print(kwargs)
    print(type(kwargs))
my_print(first_number="5", second_number=1, bool_number=True)

# ARGS AND KWARGS

def check_arguments_keywordedarguments (required_arg, *args, **kwargs):
    print(required_arg)
    if args:
        print(args)
    if kwargs:
        print(kwargs)

check_arguments_keywordedarguments("required argument")
check_arguments_keywordedarguments("required argument", 1, 2, 'hey')
check_arguments_keywordedarguments("required argument", 1, 2, 'hey', name="Sarah", age=24)



def check(a, b, c):
    print(a, b, c)

a = [1, 2, 3]
check(*a) # stessa cosa se scrivi print(a[1], a[2], c[3])

a = {"a":"Sarah", "b": 24, "c":"coding"}
check(**a)


# MAP

def upper_string(s):
    return s.upper()

fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]

for index, value in enumerate(fruit):
    fruit[index] = upper_string(value)

print(list(fruit))

# FILTER

def starts_with_A(s):
    return s[0] == "A"

fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
filtered_object = filter(starts_with_A, fruit)

print(list(filtered_object))

# REDUCE

from functools import reduce

def sum_numbers(first, second):
    return first+second

my_list = [1, 3, 5, 7]
reduced_list = reduce(sum_numbers, my_list)

print(reduced_list)


my_list = ["1", "@", "2", "5"]
my_str = "1@25"

def concat_string(first_letter, second_letter):
    return first_letter + second_letter

my_final_str = reduce(concat_string, my_list)
print(my_final_str)