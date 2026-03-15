class Farm:

    def __init__(self, farm_name = "McDonald"):
        self.farm_name = farm_name
        self.animals_list = {}
    

    def add_animal(self, animal_type, count = 1):
        if animal_type in self.animals_list:
            self.animals_list[animal_type] += count
        else:
            self.animals_list[animal_type] = count
        

    def get_info(self):
        info = f"{self.farm_name} Farm\n"
        for animal, count in self.animals_list.items():
            info += f"{animal} : {count}\n"
        info += "EIEI-0!"
        return info
       
        

# Test the code 
farm = Farm("McDonald")
farm.add_animal('cow', 5)
farm.add_animal('sheep')
farm.add_animal('sheep')
farm.add_animal('goat', 12)
print(farm.get_info())
# #output:
# # McDonald's farm

# cow : 5
# sheep : 2
# goat : 12

#     E-I-E-I-0!