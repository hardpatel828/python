# Write a program to building Hangman game. In the game of Hangman, a clue word is given by the
# program that the player has to guess, letter by letter. The player guesses one letter at a time until the
# entire word has been guessed. (In the actual game, the player can only guess 6 letters incorrectly before
# losing).


import random

words = ["apple","banana","grape","orange","mango"]

word = random.choice(words)
guessed_word = ["_"] * len(word)

guessed_letters = []

wrong_guesses = 0
max_wrong = 6

print("Welcome to Hangman Game !")
print("Guess the word letter by letter.")

while wrong_guesses < max_wrong and "_" in guessed_word:
    print("\nWord : "," ".join(guessed_word))
    print("Wrong guesses left : ",max_wrong - wrong_guesses)
    print("Guesses letters : ",guessed_letters)

    guess = input ("Enter a letter : ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in word :
        print("Correct Guess")
        for i in range (len(word)):
            if word[i] == guess :
                guessed_word[i] = guess
    else:
        print("wrong guess !")
        wrong_guesses += 1

if "-" not in guessed_word:
    print("\nYou guessed the word",word)
else :
    print("\nGame over! The word was :",word)
