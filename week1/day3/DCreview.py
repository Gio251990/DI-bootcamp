# Copy dict and wallet from the platform

items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
wallet = "$300"

# create an empty list called basket

basket = [] # cosi si crea una lista vuota chiamata basket

# clean the data (prices and wallet)

cleaned_wallet = int(wallet.replace("$", "")) # cambia il valore del wallet da $300 a 300 rimuovendo il simbolo $

for item, price in items_purchase.items(): # si chiede di controllare ogni item e price all'interno della stringa item_purches
    cleaned_price = int(price.replace("$", "").replace(",", "")) # si chiede di rimuovere da item_purches tutti i simboli $ e le , 
   
# check if the item is affordable (check the price)

    if cleaned_price <= cleaned_wallet: # controlla se il valore del nostro wallet e' adaguato per acquistare gli oggetti in item_purches

# - if it is, add to the basket and take the price from the wallet

        basket.append(item) # aggiunge gli item al nostro basket dato che si possono comprare
        cleaned_wallet -= cleaned_price # aggiorna il valore del nostro wallet (senza il simbolo $) dopo l'acquisto
    else:
        continue # chiede di continuare con gli oggetit seguenti

# - if not, skip it

# if wwe can buy something: print the nasket in alphabetical order

if basket: 
    print(sorted(basket)) # se ci sono oggetti nel basket richiede di ordinarli alfabeticamente

# if we cannot buy anything print "Nothing"

else:
    print("Nothing") # se non ci sono oggetti nel basket richiede di scrivere Nothing come output del comando

