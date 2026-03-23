print("Hello World\n"*4 + "I Love python\n"*4)

month = int(input("Enter a number from 1 to 12 representing the months: "))
if month >= 3 and month <= 5:
    season = "Spring"
elif month >= 6 and month <= 8:
    season = "Summer"
elif month >= 9 and month <= 11:
    season = "Autumn"
elif month == 12 and month <= 2:
    season = "Winter"
else:
    print("Invalid number")

print(season)