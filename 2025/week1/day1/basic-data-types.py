# BASIC DATA TYPES

# STRING: Is text in python, written in between "", a sequence of characters
# STRING METHODS

# .lower() fa diventare il testo nella stringa minuscolo (dopo la stringa)
# .upper() fa diventare il testo nella stringa maiuscolo (dopo la stringa)
# replace sostituisce una parola con un'altra all'interno di una stringa
# len conta il numero di caratteri nella stringa compresi gli spazi (prima della stringa)
# type ti dice il tipo di stringa (prima della stringa)

# NUMBERS: INTEGERS, FLOATS, COMPLEX
# INTEGERS = numeri interi - COMANDO: int()
# FLOATS = numeri decimali - COMANDO: float()

# / effettua la divisione
# % fornisce come risultato il resto a seguito della divisione

# CASTING TYPES

# BOOLEANS: True/False values (sempre con lettera iniziale maiuscola) - COMANDO: bool

# NoneType: nothing, None

# "Giovanni"+"Spizzichino" = GiovanniSpizzichino
# "Giovanni " + "Spizzichino" = Giovanni Spizzichino
# "Giovanni\t" + "Spizzichino" = Giovanni Spizzichino

my_name = "Giovanni"
name_upper = my_name.upper()

print(my_name.upper())

#STRING ARE IMMUTABLE

# my_name [0] = "G"

# SPECIAL CHARACTERS IN STRINGS
sentence = "I love Python" 
print(sentence * 3)

sentence = "I love Python\n" # Con \n va a capo ogni volta e le frasi non sono tutte sulla stessa linea
print(sentence * 3)

sentence = "I love Python\t" # con \t mette lo spazio tra le frasi
print(sentence * 3)

sentence_js = sentence.replace ("Python", "JavaScript")
print(sentence_js)

price = "15$"

clean_price = int(price.replace("$" , ""))
print(clean_price)

description = "strings are..."

print(description.upper())

description = description.replace("are" , "is")
print(description)

# STRING SLICING
print(description[:7]) # Con questo comando viene rimosso tutto quello che va oltre i primi caratteri oltre il settimo. In sostanza mantiene tutto quello che c'e' prima

# VARIABLES

f_name = "Harry"
l_name = "Potter"
age = "15"
address = "Privet Drive 4"
is_wizzard = True

# HOW TO NAME THEM: BEST PRACTICES
# DON'T START WITH NUMBERS OR SPECIAL CHARACTERS (EXAMPLE OF NOT GOOD: 14 = "MY FAVORITE NUMBER")
# USE: SHORT NAMES, IN PYTHON IS BETTER TO USE UNDERSCORE AS SPACE

first_name = "Ron"
calculation = 5+6
print(calculation)

general_var = "Hello"
general_var = 456
general_var = True
print(general_var)

# The variable doesn't store the expression, but the output of the expression

x = 1
y = 2

# Try to swap the values of x and y

temp = y # blocco il valore di y
y = x # do il comando di y = x, y = 1
x = temp # do il comando x = valore bloccato di y, x = 2
print(x, y)

# Useful function:
# Print() - It shows something defined onthe bracksts on the terminal
# input() - prompt the user for some input

user_name = input("Enter your name: ")
print(user_name)
age = input("Enter your age ") # si possono inserire solo numeri relativi all'eta', ad esempio non cincepisce somme o altre funzioni
print(age)
age = int(input("Enter your age ")) # aggiungendo la funzione int si possono creare formule
print(age + 10)
# print(user_name + "is" + age + "years old") NON FUNZIONA PERCHE AGE e' UN NUMERO INTEGER TRAMITE IL COMANDO PRECEDENTE

# f strings = the f is stand for format()

print(f"{user_name} is {age} years old")

# Increment a variable
count = 0
user_name = input("Enter your name: ")
count += 1
print(user_name)
print(count)

age = int(input("Enter you age: "))
print(f"You will turn 100 in {100-age} years")

