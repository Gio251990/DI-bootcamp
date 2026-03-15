import os
import random
import json


def get_words_from_file():

    get_words_from_file = os.path.dirname(os.path.realpath(__file__))
    with open(get_words_from_file + "\words.txt", "r") as f:
        return f.read().split()
    

def get_random_sentence(length):
    words = get_words_from_file()
    random_words = []
    for _ in range(length):
        random_words.append(random.choice(words))
    return " ".join(random_words).lower()

print(get_random_sentence(5))    

def main():
    try:
        user_input = input("Please enter a value regarding the length time between 2 and 20: ")
        length = int(user_input)
        if 2 <= length <= 20:
            sentence = get_random_sentence(length)
            print(sentence)
        else:
            print("Invalid value")
    except ValueError:
        print("Invalid input: please enter a number")

main()    




dir_path = os.path.dirname(os.path.realpath(__file__))

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "birth_date": "1990-09-25",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""


data = json.loads(sampleJson)
print(data["company"]["employee"]["payable"]["salary"])

with open(dir_path + "\sampleJson.json" , "w") as f:
    json.dump(data, f, indent = 2, sort_keys=True)
    print("file was created")



