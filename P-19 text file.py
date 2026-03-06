# Given file name of .txt file that has a list of a bunch of names, count how many of each name there are
# in the file, and print out the results to the screen.

# Hangman Game Program

# Secret word given by the program
secret_word = "python"

# To store guessed letters
guessed_letters = []

# Maximum wrong guesses allowed
chances = 6

print("🎮 Welcome to Hangman Game!")
print("Guess the word letter by letter")

# Game loop
while chances > 0:
    display_word = ""

    # Show the word with guessed letters
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if player has guessed the whole word
    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word correctly.")
        break

    # Take user input
    guess = input("Enter a letter: ").lower()

    # Check the guessed letter
    if guess in guessed_letters:
        print("You already guessed this letter.")
    elif guess in secret_word:
        guessed_letters.append(guess)
        print("✅ Correct guess!")
    else:
        guessed_letters.append(guess)
        chances -= 1
        print("❌ Wrong guess!")
        print("Remaining chances:", chances)

# If chances are over
if chances == 0:
    print("\n💀 Game Over!")
    print("The correct word was:", secret_word)