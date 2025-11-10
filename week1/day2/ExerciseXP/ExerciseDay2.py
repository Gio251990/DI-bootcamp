# Exercise 1

my_fav_numbers = [7, 10, 11, 18]
my_fav_numbers.append(5)
my_fav_numbers.append(22)
my_fav_numbers.remove(5)
my_fav_numbers.remove(22)
print(my_fav_numbers)

friend_fav_numbers = [9, 19, 3, 15]
our_fav_numbers = (my_fav_numbers + friend_fav_numbers)
print(our_fav_numbers)

# Exercise 2

tup = (1, 2, 3, 4 ,5)
second_tup = tup + (6, 7)
print(second_tup)

# Exercise 3

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0, "Apples")
count_apples = basket.count("Apples")
print(count_apples)
basket.clear()
print(basket)

# Exercise 4

list = [1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]

mysum = 1.5
while mysum < 5.5:
    print(mysum)
    mysum = mysum + 0.5

# Exercise 5

for item in range(1, 21):
    print(item)

for item in range(1, 21):
   if item % 2 == 0:
    print(item)

# Exercise 6

name = input("Enter your name ")
if not name.isdigit() and len(name) >= 3:
    print("Thank you") 
else:
    print("Enter a valid name")

# Exercise 7

favorite_fruits = input("Enter your favorite fruits ").split()
fruit = input("Enter the name of any fruit ")
if fruit in favorite_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")

# Exercise 8

toppings = []
topping = input("Enter pizza toppings one by one and type quit to finish: ")
base_price = 10
topping_price = 2.5

while topping != "quit":
    toppings.append(topping)
    print(f"adding {topping} to your pizza")
    topping = input("Enter pizza toppings one by one and type quit to finish: ")

total_cost = base_price + (len(toppings) * topping_price)

print("Your pizza has the following toppings: ")

for topping in toppings:
    print(topping)

print(f"Total Cost: ${total_cost}")

# Exercise 9

ticket_price_children = 0
ticket_price_young = 10
ticket_price_senior = 15

senior = []
young = []
children = []

client_age = int(input("How old are you? Write -1 when you are done "))

while client_age != -1:

    if client_age <3:
        children.append(client_age)
        print(f"Cinema's tickets are free for children aged {client_age} years old")

    elif client_age >=3 and client_age <12:
        young.append(client_age)
        print(f"Children aged between 3 and 12 pay ${ticket_price_young}")

    else:
        print(f"Clients over the age of 12 pay ${ticket_price_senior}")
        senior.append(client_age)

    client_age = int(input("How old are you? Write -1 when you are done "))

total_price = (len(senior)*ticket_price_senior) + (len(young)*ticket_price_young)
print(f"Total cost: ${total_price}")

