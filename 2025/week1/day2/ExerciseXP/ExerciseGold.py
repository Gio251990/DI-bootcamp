list1 = ["banana", "apple", "cherry"]
list2 = ["orange", "watermelon", "lemon"]

list1.extend(list2)
print(list1)

# list1 = ["banana", "apple", "cherry"]
# list2 = ["orange", "watermelon", "lemon"]

# print(list1 + list2)

number = range(1500, 2501, 5)
for n in number:
    print(n)

number = range(1500, 2501, 7)
for n in number:
    print(n)

for number in range(1500, 2501):
    if number % 5 == 0 and number % 7 == 0:
        print(number)




names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
