import random

# List of predefined words
words = ["apple", "brain", "cloud", "train", "zebra"]

# Choose a random word
word = random.choice(words)
word_letters = list(word)
guessed_letters = []
incorrect_guesses = 0
max_guesses = 6

print("Welcome to Hangman!")
print("_ " * len(word))

# Game loop
while incorrect_guesses < max_guesses:
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You've already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word_letters:
        print("Correct!")
    else:
        incorrect_guesses += 1
        print(f"Wrong! You have {max_guesses - incorrect_guesses} guesses left.")

    # Display current word progress
    display_word = [letter if letter in guessed_letters else "_" for letter in word]
    print(" ".join(display_word))

    # Check for win
    if "_" not in display_word:
        print("Congratulations! You guessed the word:", word)
        break

# Check for loss
if incorrect_guesses == max_guesses:
    print("Game Over! The word was:", word)
