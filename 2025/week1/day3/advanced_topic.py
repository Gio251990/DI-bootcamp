# LOOPS OPERATOR

# SYNTAX OF A FOR LOOP:
# for <variable> in <sequence>               sequence: list, string, etc
# _____ an intended block of code (will happen within each iteration)

# range() - helps us to create a sequence of numbers (start=0, stop, step=1)
for num in range(1, 10): # con (1, 10) si specifica 1 come partenza e non 0 come default e 10 come numero finale ma non incluso
    print(num)

for num in range(1, 10, 3): #il terzo parametro step, indica la decadenza. Impostando 2, salta i numeri ogni 2 es. 1,3,7,9
    print(num)

# enumerate() - gives as a tuple with index and item
student_info1 = ["Harry", "Potter", 15, "Privet Drive, 4", "Hedwig", "Buckbeak"]

student_info1[0] = student_info1[0].lower() # per farlo una sola volta 

# let's chenge the items that are string to lowercase

for item in student_info1:
    if type(item) == str:
        item.lower()
print(student_info1)

for i, item in enumerate(student_info1): # using enumerate() we have access to bot: index and item
    if type(item) == str: # we check if the item is string type
        student_info1[i] = item.lower() # we reasign the item to its lowercase version
print(student_info1)

# not for loop related: just useful in general:
# zip() - can be used of any kind of sequence

name = ["Juliana", "Jeremy", "Avner", "Sonia"]
cities = ["Ramat Gan", "Modiin", "Raanana", "Tel Aviv"]

#name_cities = {"Juliana":"Ramat Gan"} - to do that we can use zip()

name_cities = dict(zip(name, cities))
print(name_cities)
