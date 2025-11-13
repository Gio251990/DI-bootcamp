# DAY 1 IS OK
# DAY 2

# LIST = Mutable, Ordered sequence

friends = ["Ross", "Rachel", "Monica", "Joey", "Chandler", "Phoebe"]

print(friends[2])
print(friends[2:5]) # slicing

# List methods

friends.append("Juliana") # aggiunge un valore alla lista all'ultimo posto
friends.insert(2, "Juliana") # inserisce il nome scelto prima dell'intervallo scelto
friends.remove("Monica") # rimuove il valore scelto
del friends[2] # altra soluzione per rimuovere un valore specificando la posizione (sempre partendo da 0)
poped_value = friends.pop(-2) # pop rimuove il valore dalla lista e lo tiene in memoria
print(f"Bye Bye {poped_value}")
print(friends)

# sort()
print(friends)
friends.sort()
print(friends)
# sorted()
print(friends)
sorted_friends = sorted(friends) # ordina la lista in ordine alfabetico
print(sorted_friends)

# split()
user_info = input("Enter your name and age separated by comma: ").split(", ")
print(user_info)

# join() is a str method that needs a sequence as arguments
students = input("Enter the students name: ").split()

print(f"The new students are: {", ".join(students)}")

# LOOPS

# FOR LOOP
# Synthax:
# for <variable> in <sequence>:
#    an indented block of code

for student_name in students:
    print(f"Welcome, {student_name}")

output = []
for num in range(1,6):
    output.append(num)
    output.append(num + 0.5)
print(output[1,-1])

# WHILE

toppings_list = []
price = 10

while True:
    topping = input("Enter the topping or 'q' for quit").lower()
    if topping == "q":
        if toppings_list:
            print(f"Your toppings are: {", ".join(toppings_list)} and this is the total price: {price}")
            break
        else:
            print(f"You didn't choose and topping and price is {price}")
            break
    else:
        toppings_list.append(topping)
        price += 2.50
        print(f"The {topping} were added to ypur pizza")




