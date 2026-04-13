word = input("Insert a word: ")

result = {}

for i, letter in enumerate(word):
    if letter in result:
        result[letter].append(i)
    else:
        result[letter] = [i]

print(result)



items_purchase = {
    "Water": "$1",
    "Bread": "$3",
    "TV": "$1,000",
    "Fertilizer": "$20"
}

wallet = "$300"

money = int(wallet.replace("$", "").replace(",", ""))

basket = []

for item in items_purchase:
    price = int(items_purchase[item].replace("$", "").replace(",", ""))

    if price <= money:
        basket.append(item)
        money -= price

if not basket:
    print("Nothing")
else:
    print(sorted(basket))