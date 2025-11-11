# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

# key_value = dict(zip(keys, values))
# print(key_value)



# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
# ticket_price_children = 0
# ticket_price_young = 10
# ticket_price_senior = 15

# total_price = 0

# for key, value in family.items():
#     if value < 3:
#         price = ticket_price_children
#     elif value >=3 and value < 12:
#         price = ticket_price_young
#     else:
#         price = ticket_price_senior

#     print(f"{key.title()}'s ticket price: ${price}")

#     total_price += price

# print(f"Total price fot the family is ${total_price}")




# brand = {"name" : "Zara",
#         "creation_date" : 1975,
#         "creator_name" : ["Amancio" , "Ortega" , "Gaona"],
#         "type_of_clothes" : ["men" , "women" , "children" , "home"],
#         "international_competitors" : ["Gap" , "H&M" , "Benetton"],
#         "number_stores" : 7000,
#         "major_color" : [
#             {"France" : "blue"}, 
#             {"Spain" : "red"}, 
#             {"US": ["pink" , "green"]}]
#         }
# brand["number_stores"] = 2
# print(f"Zara's client are {brand['type_of_clothes']}")
# brand.update({"country_creation" : "Spain"})
# if "international_competitors" in brand:
#     brand["international_competitors"].append("Desigual")
# del brand["creation_date"]
# print(brand["international_competitors"][-1])
# print(brand["major_color"][2])
# print(len(brand))
# print(list(brand.keys()))
# print(brand)



users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
