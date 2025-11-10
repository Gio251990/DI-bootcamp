string = input("Write a sentence of exactly 10 characters long ")
number_of_characters = len(string)
if number_of_characters < 10:
    print("String not long enough")
elif number_of_characters > 10:
    print("String too long")
else:
    print("Perfect string")

print(string[0:1], string[9:10])

print(string[:1])
print(string[:2])
print(string[:3])
print(string[:4])
print(string[:5])
print(string[:6])
print(string[:7])
print(string[:8])
print(string[:9])
print(string[:10])