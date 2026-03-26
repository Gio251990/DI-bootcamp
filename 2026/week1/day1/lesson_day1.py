print("Hello Word")
print(8+3) # somma
print(8-3) # sottrazione
print(8/2) # divisione con decimale
print(8//3) # quante volte il numero e' divisibile
print(4*2) # moltiplicazione
print(8%3) # resto della divisione (modulo)

# BASIC VALUE TYPES

# - STRING (frasi)     "Hello World"
# - NUMBERS (numeri)   "5"
# - BOOLEAN (vero/falso)   4<3 - False

# TYPE - tipo di classe
print(type("hello"))
print(type(True))
print(type(4))

# STRING FUNCTIONS
# .upper()        # MAIUSCOLO
# .lower()        # minuscolo
# .capitalize()   # Prima lettera maiuscola
# .title()        # Ogni parola maiuscola
# .swapcase()     # Inverte maiuscole/minuscole
# .replace()      # Sostituisce testo
# .strip()        # Rimuove spazi inizio/fine
# .lstrip()       # Rimuove spazi a sinistra
# .rstrip()       # Rimuove spazi a destra
# .find()         # Trova posizione (o -1)
# .index()        # Trova posizione (errore se non trova)
# .count()        # Conta occorrenze
# .startswith()   # Controlla inizio
# .endswith()     # Controlla fine
# .isalpha()      # Solo lettere
# .isdigit()      # Solo numeri
# .isalnum()      # Lettere + numeri
# .isspace()      # Solo spazi
# .islower()      # Tutto minuscolo
# .isupper()      # Tutto maiuscolo
# .split()        # Divide in lista
# .join()         # Unisce lista in stringa
# len()           # Lunghezza stringa
# []              # Accesso per indice
# [start:end]     # Slice
# .format()       # Formattazione
# f""             # f-string (consigliato)
# .center()       # Centra testo
# .ljust()        # Allinea a sinistra
# .rjust()        # Allinea a destra
# .removeprefix() # Rimuove prefisso
# .removesuffix() # Rimuove suffisso
# .casefold()     # Versione avanzata di lower()

description = "strings are..."
print(description.upper())   # tutto maiuscolo
print(description.replace("are", "is"))   # sostituisce due parole
print(description.split()[0])   # fa in modo di mostrare sola la prima parola avendo messo 0
print(description.replace(" are...",""))   # altro modo per fare in modo che venga mostrata solo la sezione di interesse eliminando il resto, in questo modo abbiamo sostituito un valore con "" che non mostra nulla


# NUMBERS
# - INTEGERS - interi
# - FLOATS - frazionari

print(type(5.3)) # risultato float

my_Age = 35
print(my_Age + 123879)

print(type(10))
print(type(str(10))) # converte la class da integer a string

print("Hello World "*2) # scrive la stringa 2 volte
print(int("2")*3) # converte la stringa in integer ed effettua la moltiplicazione facendo in modo che risulta un numero e non una stringa ripetuta piu' volte

bank_balance = '33000'
phone_number = 532287514

print(int(bank_balance)) # converte in integer
print(str(phone_number)) # converte in string

first_name = "Giovanni"
last_name = "Spizzichino"
print((first_name )+ " " +(last_name)) # fa in modo che il comando riconosca lo spazio tra le due stringhe, senza " " le stringhe risulterebbero unite senza spazio

print("Hello world\nMy name is Rick") # \n manda a capo
print("Peace on the\tWORLD") # \t applica 4 spazi


# BOOLEANS
# - True
# - False

print(3>4) # risultato false
print(4>=4) # risultato true

# >	    Greater that - True if left operand is greater than the right	                                 x > y
# <	    Less that - True if left operand is less than the right	                                         x < y
# ==	Equal to - True if both operands are equal	                                                     x == y
# !=	Not equal to - True if operands are not equal	                                                 x != y
# >=	Greater than or equal to - True if left operand is greater than or equal to the right	         x >= y
# <=	Less than or equal to - True if left operand is less than or equal to the right	                 x <= y

print(3 < 4 or 2 > 1) # true se almeno una delle due operazioni
print(3 < 4 and 2 > 1) # true se tutte e due le operazioni sono vere


x = 5
y = 10
z = 0
word1 = "hello"
word2 = "world"

print(x<y and y>z)
print(word1 == word2)
print(bool(z))
print(bool(word1))


my_name = "Giovanni"
my_age = "35"
print("My name is " + my_name + ", and I am " + my_age + " years old.")

my_hair_color = "black"
print(my_hair_color)

my_number = 5
my_number = my_number + 1
# my_number += 1          stessa cosa

print(my_number)

name = "Frank"
age = 65

print(f"Hello, {name}. You are {age}.")
print("Hello, {}. You are {}.".format(name, age)) # stessa cosa meno usata

# IF STATEMENT

a = 33
b = 200
if a > b:
    print("a is greater than b")
elif a == b:
    print("a is equal to b")
elif a < b:
    print("a is lower than b")
print("Finished")


name = input('Please state your name: ')

if name == 'Frank':
  print('You are Frank Sinatra')
elif name == 'Miles':
  print('You are Miles Davis')
elif name == 'Tony':
  print('You are Tony Benett')
else:
  print('I do not know who you are!')


# AND CONDITION tutte e due le condizioni devono essere corrette
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

# OR CONDITION almeno una delle due condizioni deve essere corretta

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

# IN (NOT e' il suo opposto)

my_hobbies = "sport, code, food, icecreams, netflix"
if "code" in my_hobbies:
    print("Hello world")


number = int(input("Enter a number between 1 and 100: "))
if number % 3 == 0 and number % 5 == 0:  # mettendo la condizione come prima si da priorita' visto che if e elif convalidano immediatamente la prima condizione e passano alla successiva solo se falsa
   print("FizzBuzz")
elif number % 5 == 0:
   print("Buzz")
elif number % 3 == 0:
   print("Fizz")
