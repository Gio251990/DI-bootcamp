mylist = ["apple", "banana", "cherry", 12, 1.09, True]
# print(mylist)
# print(mylist[-1])
# print(mylist[-2])

mylist[1] = "Pinapple"

newlist = ["apple", "banana", "cherry", [1, 4, 7]]
print(newlist)

inside_list = newlist[3]
print("insidelist")
print(inside_list)
print("newlist[3]")
print(newlist[3])

grid = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]
print(grid[0][0]) # nelle prime parentesi quadre si richiede quale griglia e nelle seconde quale parte della griglia partendo sempre da 0

# Adding items at the end of my list

mylist.append("this is the new last item") # con questo comando si aggiungono parti alle liste create
print(mylist)

mylist.remove("cherry") # con questo comando si rimuove qualcosa dalle liste
print(mylist)

duplicates = ["first", "second", "first", "third"]
duplicates.remove("first")
print(duplicates)

third_item = duplicates.pop(2) # rimuove una specifica parte della lista partendo sempre da 0 per il primo elemento
print(duplicates)
print(third_item)

first = [1, 2, 3, 4]
second = [5, 6, 7, 8]

first.extend(second) # allinea le due liste create
print(first)

print(first + second) # allinea le due liste senza unirle in un unica stringa (verranno sempre chiamate separatamente)

print(first*3)
print(len(first)) # con "len" si contano il numero di caratteri nell'elemento scelto
print(sum(first)) # somma i valori all'interno dell'elemento
print(max(first)) # fornisce il valore massimo
print(min(first)) # fornisce il valore minimo

print(max([[1, 2, 3], [4, 5, 6], [7, 8, 9]])) # fornisce la lista con valore maggiore sommando i numeri all'interno

# TUPLES

tup = (1, 2, 3, 4, "Happy Birthday") # a differenza delle liste, tuples non possono essere modificati
print(tup)

a, b, c, d, e = tup
print(a)
print(b)
print(c)
print(d)
print(e)

# SET

s = set([1, 2, 2 ,5 ,5, 6]) # set non fornisce valori duplicati e non garantisce che vengano messi in ordine
print(s)
s.add(10) # 10 viene aggiunto in quanto numero mancante
print(s)
s.add(2) # 2 non viene aggiunto in quanto numero presente nella lista
print(s)

# LOOPS

li = [12, 15, 264, 234, 12, 577, 109]
for item in li: # il comando chiede di esaminare ogni singolo item nella lista
    if item > 200: # con questa aggiunta richiede di scrivere solamente tutti i numeri > di 200 presenti nella lista
        print("Big number is", item)
    else:
        print("Small number is", item)

mysum = 0
for item in li:
    mysum = mysum + item
    print("current sum: ", mysum)
    print("Final sum: ", mysum)

i = 0
while i < 10:
    print(i)
    i = i + 1    # fornisce tutti i numeri precedenti al valore indicato es. i < 10 fornisce tutti i numeri fino a 9

j = 0
while j < len(li):
    print(li[j])
    j = j + 1

password = "secret"
guess = input("waht is your password? ")
while guess != password:             # crea richieste infinite ogni volta che l'utente fornisce passord errate
    print("Incorrect password")
    guess = input("What is the password? ")

print("Correct password") 

# Continue

i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue  # fa continuare a cercare soluzioni fino al raggiungimento del valore impostato nel nostro caso < 10
    print(i)

# Break

li = [12, 15, 264, 234, 12, 577, 109]

for item in li:
    if item > 500:
        print("Big number found: ", item)
        break
    print(item)
    print("random things happening until i find what im looking")


