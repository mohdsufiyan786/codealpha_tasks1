import random

# Word list
words = ["codealpha", "website", "mango", "india", "city"]

# Randomly choose a word
word = random.choice(words)

# Convert word to list of characters
word_letters = list(word)

# Underscore display
guess_display = ["_"] * len(word)

# Already guessed letters
guessed_letters = []

# Number of wrong tries allowed
tries = 6

print("Welcome to Hangman!")
print("Guess the word:")

# Game loop
while tries > 0 and "_" in guess_display:
    print("\nWord: ", " ".join(guess_display))
    print("Guessed letters:", guessed_letters)
    print("Tries left:", tries)

    guess = input("Enter a letter: ").lower()

    # STEP 1: Check if valid single alphabet
    if len(guess) != 1 or not guess.isalpha():
        print(" Please enter a valid **single alphabet letter**.")
        continue

    # STEP 2: Check if already guessed
    if guess in guessed_letters:
        print(" You already guessed that letter!")
        continue

    # STEP 3: Add to guessed letters list
    guessed_letters.append(guess)

    # STEP 4: Check if letter in word
    if guess in word_letters:
        print(" Correct guess!")
        for i in range(len(word)):
            if word[i] == guess:
                guess_display[i] = guess
    else:
        print(" Wrong guess!")
        tries -= 1  # Only wrong guess reduces chance

# GAME RESULT
if "_" not in guess_display:
    print("\n Congratulations! You guessed the word:", word)
else:
    print("\n You lost! The word was:", word)
