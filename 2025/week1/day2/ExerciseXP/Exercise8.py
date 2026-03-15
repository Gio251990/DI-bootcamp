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