import random

wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
word = random.choice(wordslist)

guessed_letters = []
wrong_guesses = 0
max_wrong = 6

display = []
for char in word:
    if char == " ":
        display.append(" ")
    else:
        display.append("*")

print("Welcome to Hangman!")

while wrong_guesses < max_wrong and "*" in display:
    print("\nWord:", "".join(display))
    print("Guessed letters:", guessed_letters)
    
    guess = input("Guess a letter: ").lower()
    
    if len(guess) != 1 or not guess.isalpha():
        print("Insert a single valid letter.")
        continue
    
    if guess in guessed_letters:
        print("You already guessed this letter.")
        continue
    
    guessed_letters.append(guess)
    
    if guess in word:

        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
        print("Correct!")
    else:
        wrong_guesses += 1
        print("Wrong! Body part added:", wrong_guesses, "/6")


if "*" not in display:
    print("\nYou won! The word was:", word)
else:
    print("\nYou lost! The word was:", word)