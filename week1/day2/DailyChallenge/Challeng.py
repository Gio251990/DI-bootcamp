number = int(input("Please enter a number "))
length = int(input("Please enter a length "))

multiples = []

for i in range(1, length + 1):
    multiples.append(number * i)

print(multiples)



string = input("Enter a string ")
s = set(string)
print(s)