number = int(input("Please enter a number "))
length = int(input("Please enter a length "))

multiples = []

for i in range(1, length + 1):
    multiples.append(number * i)

print(multiples)



string = input("Enter a string: ")

new_string = ""
for i in range(len(string)):
    if i == 0 or string[i] != string[i - 1]:
        new_string += string[i]

print(new_string)