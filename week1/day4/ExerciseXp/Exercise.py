def Display_message():
    print("I am learning about functions in Python.")

Display_message()



def favorite_book(title):
    print(f"One of my favorite book is {title}")

favorite_book("Harry Potter")



def describe_city(city, country = "Unknown"):
  
    print(f"{city} is in {country}")

describe_city("Rome", "Italy")



import random

def compare_num(user_num):
    computer_num = random.randint(1, 100)
    if user_num == computer_num:
        print("Success!")
    else:
        print(f"{computer_num}, Fail")
    
compare_num(50)



def make_shirt(size, text = "I love Python"):
    if size == "large":
        print(f"The size of the shirt is {size} and the text is {text}")
    elif size == "medium":
        print(f"The size of the shirt is {size} and the text is {text}")
    elif size == "small":
        print(f"The size of the shirt is {size} and the text is {text}")

make_shirt("large", "I love Italy")



magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magician(*args):
    if args:
        for name in args:
            print(name)
    
show_magician('Harry Houdini', 'David Blaine', 'Criss Angel')

def make_great(*args):
    for name in args:
        print(f"{name} the Great")

make_great('Harry Houdini', 'David Blaine', 'Criss Angel')



import random

def get_random_temp():
    temp = random.randint(-10, 40)
    return temp

def main(temp):
    temp = get_random_temp()
    print(f"The temperature right now is {temp} degrees Celsius.")
    if temp < 0:
        print("Brrr, that's freezing! Wear some extra layers today.")
    elif temp >= 0 and temp < 16:
        print("Quite chilly! Don’t forget your coat.")
    elif temp >= 16 and temp <= 23:
        print("Nice weather.")
    elif temp >= 24 and temp < 32:
        print("A bit warm, stay hydrated.")
    elif temp > 32 and temp <= 40:
        print("It’s really hot! Stay cool.")

main(20)

