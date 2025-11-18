user_input = input("Enter words separated by commas: ")
words_list = user_input.split(",")
words_list.sort()
sorted_string = ",".join(words_list)
print(sorted_string)



def longest_word(sentence):
    words = sentence.split()
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

print(longest_word("Margaret's toy is a pretty doll."))       
print(longest_word("A thing of beauty is a joy forever."))    
print(longest_word("Forgetfulness is by all means powerless!"))