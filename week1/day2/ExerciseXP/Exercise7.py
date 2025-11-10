favorite_fruits = input("Enter your favorite fruits ").split()
fruit = input("Enter the name of any fruit ")
if fruit in favorite_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")

