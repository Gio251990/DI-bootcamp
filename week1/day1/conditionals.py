# CONDITIONALS

#LOGIC OPERATORS
print(5 == "5") # equal
print(5 != "5") # different
print(5 < 3) # less then
print(5 <= 5) # less or equal then
print( 5 > 2) # greater then

# syntax of conditional expression:

# if <condition>:
#   an indented block of code

client_age = int(input("What\'s your age? "))
if client_age <= 12:
    print("Sorry, you can\'t see the movie")

elif client_age >= 13 and client_age <= 16:
    print("You can see the movie with your parents")

else:
    print("You can see the movie") # Se ci sono due IF e' meglio mettere un secondo ELIF al posto di ELSE alla fine