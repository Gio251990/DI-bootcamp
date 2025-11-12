# Recap of day 2
# DATA STRUCTURE - SENTENCES

# - LIST: MUTABLE, ORDERED
# - TUPLES: UNMUTABLE, ORDERED
# - SETS: MUTABLE, ORDERED, DON'T ACCEPT REPEATED ITEMS

# - SEQUENCES METHOD
# - LOOPS

# DICTIONARIES: COMPLEX DATA STRUCTURE

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




# accessing data
print(student_info["first_name"])
print(student_info["pets"][1])
print(student_info["houses"]["main"])

# how to use methods on dictionary values

student_info["pets"].append("Toby")
print(student_info["first_name"].upper())

# changing values of a dictionary

student_info[0] = "Tiago"
student_info["first_name"] = "Tiago"

# Breackets (Parentesi):
# () per Tuples
# [] per index
# {} per dictionaries

# set vs dictionary
my_set = {"Israel", "US", "Brazil"}
my_name = {"name": "Juliana"}

# Exercise
# print harry's age
print(student_info["age"])
# add 10 yo and print again
student_info["age"] += 10
print(student_info["age"])
# change address to Betzalel 8
student_info[3] = "Betzalel 8"
student_info["address"] = "Betzalel 8"
print(student_info["address"])
# add a new pet to the list
student_info["pets"].append("Bob")
print(student_info["pets"])
# change is parselmouth to false
student_info["is_parselmouth"] = False
print(student_info["is_parselmouth"])

# How to add a new key: value pair
student_info["Teachers"] = "Snap" # option 1
student_info.update({"Principal" : "Dumbleadore"}) # option 2

print(student_info)

# Exercise

sample_dict = { 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}

print(sample_dict["class"]["student"]["marks"]["history"])