word = input("Enter a word: ")
char_dict = {}

for index, char in enumerate(word):
    if char in char_dict:
        char_dict[char].append(index)
    else:
        char_dict[char] = [index]
print(char_dict)



items_purchase = {"Phone": "$999", "Speakers": "$300", "Laptop": "$5,000", "PC": "$1200"}
wallet = "$1"

basket = []

money = int(wallet.replace("$", "").replace(",", ""))

for item in items_purchase:
    price = int(items_purchase[item].replace("$", "").replace(",", ""))
    if price <= money:
        basket.append(item)
        money -= price

if len(basket) == 0:
    print("Nothing")
else:
    basket.sort()
    print(basket)



