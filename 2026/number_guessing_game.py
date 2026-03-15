import random
def number_guessing_game(min_val=1, max_val=100, max_attempts=7):

    random_number = random.randint(min_val, max_val)
    print(f"I have chosen a number between {min_val} and {max_val}. You have {max_attempts} attempts!")

    for attempt_num in range(1, max_attempts + 1):
        guess = int(input("Please enter a value between 1 and 100: "))
        if guess == random_number:
            print("Number found")
            return
        elif guess < random_number:
            print("Too low!")
        elif guess > random_number:
            print("Too high!")
    print(f"Too bad! You've used up all your attempts. The number was {random_number}.")

number_guessing_game()