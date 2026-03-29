# DITCIONARIES

Bob = {
    "name" : "Bob",
    "age" : 10
}

print(Bob["age"])


rick_dict = {
    'first_name':'Rick',
    'last_name':'Sanchez'
}
print("The last name of rick is:", rick_dict['last_name'])

rick_dict["age" ] = 10

print(rick_dict)


# student = {"name": "alice", "age": 10, True: "its valid", ("a", "b"): "something"}

# print(student.keys())

# for key and value in student.item():
#    print(f"key: item{0}, value: {item[1]}")

dict1 = {
    "number1": 1,
    "number2": 2,
    "number3": 4
}

dict2 = {
    "number2": 22,
    "number5": 5
}

dict1.update(dict2)
print(dict1)


sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}

keys_to_remove = ["name", "salary"]

for key in keys_to_remove:
    del sample_dict[key]

print(sample_dict)


my_books = {
  "title": "Harry Potter",
  "author": "JK Rowling",
}

for x, y in my_books.items():
    print("the " + x + " is " + y)


print(list(range(1, 20, 2))) # 1 = start, 2 = stop, 3 = step ovvero ogni quanto deve passare il range

# ENUMERATE

my_str = "abcd"
print(list(enumerate(my_str)))

for index, value in enumerate(my_str):
    print(f"The letter at {index} is {value}")

# ZIP

keys = ["name", "salary"]
values = ["bob", "100"]

# dict = {
#     "name": "bob",
#     "salary": "100"
# }

dict = {}

zipped_items = zip(keys, values)
for key, value in zipped_items:
    dict[key] = value

print(dict)

# FOR ELSE

for i in range(1, 3):
    print(i)
else:
    print('The for loop is over')

# WHILE ELSE

x = 0
while x < 2:
    print(f'x is {x}')
    x += 1
else:
    print('x is bigger than 2')


top_secret_password = "1234"
number_of_tries = 0

while number_of_tries < 3:
    password = input("Please enter your password: ")
    if password == top_secret_password:
        print("Password correct!")
        break
    else:
        print("Try again")
        number_of_tries += 1
else:
    print("Game over")

# CONTINUE

for letter in 'Leonardo':
    if letter == 'o':
        continue
    print(letter, end='') # dont execute for 'o' letter

# PASS salta l'errore



