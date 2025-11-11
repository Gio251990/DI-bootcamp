word = input("Enter a word: ")
char_dict = {}

for index, char in enumerate(word):
    if char in char_dict:
        char_dict[char].append(index)
    else:
        char_dict[char] = [index]
print(char_dict)



items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
wallet = "$300"

