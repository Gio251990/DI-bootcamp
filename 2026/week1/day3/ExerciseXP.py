my_fav_numbers = {10}
my_fav_numbers.add(7)
my_fav_numbers.add(15)
my_fav_numbers.remove(15)
friend_fav_numbers = {13, 18, 21}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)

print(our_fav_numbers)


# list = int(1, 3 , 6, 5)
# list.append(10)


basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0, "Apples")
print(basket.count("Apples"))
basket.clear()
print(basket)


numbers = []
base = 0.5

for i in range(1, 5):
    numbers.append(base + i)
    numbers.append(i + 1)

print(numbers)


numbers = range(1, 21)
for number in numbers:
    print(number)

for even_numbers in numbers:
    if even_numbers % 2 == 0:
        print(even_numbers)


name = input("Enter your name: ")
if not name.isdigit() and len(name) >= 3:
    print("Thank you") 
else:
    print("Enter a valid name")


favorite_fruits = input("Enter your favorite fruits ").split()
fruit = input("Enter the name of any fruit ")
if fruit in favorite_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")



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


