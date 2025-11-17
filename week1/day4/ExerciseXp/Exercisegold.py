from datetime import date
today_date = date.today()

# year = int(input("Enter your year of birth: "))
# month = int(input("Enter your month of birth: "))
# day = int(input("Enter your day of birth: "))


date_input = input("Please enter your date of birth in yyyy/mm/dd format: ")
gender = input("Please enter your gender, f or m: ")

def get_age(year, month, day):
    date_of_birth = date(year, month, day)
    age = today_date.year - date_of_birth.year
    if (today_date.month, today_date.day) < (date_of_birth.month, date_of_birth.day):
        # print(f"You are {age-1} years old")  
        return age-1
    else:
        # print(f"You are {age} years old") 
        return age 

def can_retire(gender, date_of_birth):
    splitted_date = date_of_birth.split("/")
    year_of_birth = splitted_date[0]
    month_of_birth = splitted_date[1]
    day_of_birth = splitted_date[2]

    age = get_age(int(year_of_birth), int(month_of_birth), int(day_of_birth))
    if gender == "m" and age >= 67:
        can_be_retired = True
    elif gender == "f" and age >= 62:
        can_be_retired = True
    else:
        can_be_retired= False
    return can_be_retired

print(can_retire(gender, date_input))
