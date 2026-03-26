# LIST [MUTABLE]

number1 = 5
number2 = 4
number3 = 10

my_numbers = [number1, number2, number3] # con parentesi quadre e' una list (si possono cambiare i valori all'interno)
print(my_numbers)

print(my_numbers[0]) # con questo comando, viene mostrata solo il primo index della nostra lista, python comincia a contare da 0
print(my_numbers[-1]) # con questo comando, viene mostrata solo l'ultimo index della nostra lista
print(my_numbers.index(10)) # con questo comando, viene mostrato quale index appartiene il numero 10 in questo caso e' l'index 2

print(len(my_numbers)) # con questo comando viene mostrato il conteggio degli elementi nella nostra lista

my_numbers.append(12) # con questo comando viene aggiunto il valore richiesto () alla nostra lista come ultimo index
my_numbers.remove(12) # con questo comando viene rimosso il valore richiesto () alla nostra lista
my_numbers.pop(0) # con questo comando viene rimosso l'index richiesto nelle parentesi ()
my_numbers.insert(4, 50) # con questo comando viene aggiunto il valore richiesto (50) come indice richiesto (3)

sorted(my_numbers) # ordina i numeri all'interno della lista
sum(my_numbers) # somma i numeri all'interno della lista


print(my_numbers)
print(type(my_numbers))

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(my_list[0:4]) # vengono mostrati solamente i primi 4 index della lista perche' il valore 4 non e' compreso


# TUPLE [IMMUTABLE]

numbers = (1, "hi", True) # con parentesi tonde e' un tuple (non si possono cambiare i valori all'interno)
print(numbers[0])
print(type(numbers))

# SET (nessun ordine) [MUTALBE]

unique_names = {"Bob", "Alice", "Bob", "Jack"} # con le parentesi graffe e' un set, il comando non restituisce doppioni quindi Bob viene mostrato una sola volta
print(type(unique_names))
print(unique_names)


# FOR LOOPS

fruits = ['apple', 'banana', 'kiwi', 'pear']

for fruit in fruits:
  print(fruit) # scrive tutti i fruits all'interno della lista

cities = ["London", "San Francisco", "Paris", "Barcelona"]

for city in cities:
    print("I once went to", city)

# RANGE

numbers = range(1, 11)
for number in numbers:
    print(number)

numbers = []
for number in numbers:
   print(number)
   print(number+1)


number = int(input("Insert a number: "))

for i in range(1, 11):
    print(number * i)