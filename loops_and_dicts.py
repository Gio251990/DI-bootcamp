student_info1 = ["Harry", "Potter", 15, "Privet Drive, 4", "Hedwig", "Buckbeak"]

student_info = {"first_name":"Harry", 
                "last_name": "Potter", 
                "age": 15, 
                "address": "Privet Drive", 
                "pets":["Hedwig", "Buckbeak"], 
                "best-friends": ("Ron Wealey", "Hermione Granger"),     # parentesi tonda perche il paramento non necessita di essere cambiato 
                "is_parselmouth": True,
                "houses": {"main" : "Griffyndor", "second": "Slytherin"}
                }
# loop in a list = directly
for item in student_info1:
    print(item)

# options of loops in dictionaries:

# access only keys = keys()
for key in student_info.keys():  # scrive solamente il titoli del data es. firts_name
    print(key)

# access only keys = values()
for value in student_info.values():  # scrive solamente i parametri del data es. Harry
    print(value)

# access both: keys and values
for key, value in student_info.items(): # scrive entrambi i valori richiesti es. first_name Harry
    print(key, value)

# we want to change all the string value to upper case
for key, value in student_info.items(): # accessing both: keys and values
    if type(value) == str: # check if the value is a string
        student_info[key] = value.upper() # changing the value to UPPERCASE
print(student_info)
