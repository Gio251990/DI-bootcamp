print("Hello World " *4 ,"I love python " * 4)

mount = int(input("Enter the number for a mounth between 1 and 12: "))


if mount >= 3 and mount <= 5:
    season = "The season is Spring"
elif mount >= 6 and mount <= 8:
    season = "The season is Summer"
elif mount >= 9 and mount <= 11:
    season = "The season is Autumn"
elif mount == 12 and mount <= 2:
    season = "The season is Winter"
else:
    print("Invalid")

print(season)
