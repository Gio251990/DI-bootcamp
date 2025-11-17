# Try except block

# print("This isn't a string) 
 
      
print("This will run") # this code was not be executed because there is an error on the previous line

# Using try except block avoids that problem
while True:
    try:
        move = int(input("Enter a row and column"))
        if move < 1 or move > 3:
            print("Please enter a number between 1 and 3")
            continue
        else:
            print("move accepted")
            break
    except Exception as e:
        print(e)

