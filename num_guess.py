# Define the correct number as a constant
correct_number = 7

# Ask the user to guess a number
user_guess = int(input("Guess a number between 0 and 9: "))

# Check if the user's guess is correct
if user_guess == correct_number:
    print("You guessed correctly!")
else:
    print("You guessed wrong.")
