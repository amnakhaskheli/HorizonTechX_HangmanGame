import random

words = ["python", "laptop", "code", "intern", "developer"]
word = random.choice(words)

guessed = []
mistakes = 0

print("Welcome to Hangman!")

while mistakes < 6:
    display = ""

    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    if all(letter in guessed for letter in word):
        print("You Won!")
        break

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Enter one valid letter!")
        continue

    if guess in guessed:
        print("Already guessed!")
        continue

    guessed.append(guess)

    if guess in word:
        print("Correct guess!")
    else:
        mistakes += 1
        print("Wrong guess! Chances left:", 6 - mistakes)

if mistakes == 6:
    print("Game Over! Word was:", word)