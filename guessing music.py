import random

# List of music-related words or phrases to guess
music_words = ["pop", "rock", "klasik", "jazz", "hip-hop", "melody", "metal"]

# Choose a random word from the list
word_to_guess = random.choice(music_words)

# Convert the word to a list of individual letters
word_letters = list(word_to_guess)

# Initialize variables for tracking the game
attempts = 6  # Number of attempts allowed
guessed_letters = []  # List of letters guessed by the player

# Print a welcome message
print("Welcome to the Music Word Guessing Game!")
print("You have", attempts, "attempts to guess the word.")

# Main game loop
while attempts > 0:
    # Display the word with underscores for unguessed letters
    display_word = ""
    for letter in word_letters:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"
    
    print("Word:", display_word)
    
    # Ask the player to guess a letter
    guess = input("Guess a letter: ").lower()
    
    # Check if the guess is a single letter and hasn't been guessed already
    if len(guess) == 1 and guess.isalpha():
        if guess in guessed_letters:
            print("You've already guessed that letter.")
        elif guess in word_letters:
            guessed_letters.append(guess)
            print("Good guess!")
        else:
            guessed_letters.append(guess)
            attempts -= 1
            print("Incorrect guess. You have", attempts, "attempts left.")
    else:
        print("Please enter a valid single letter.")
    
    # Check if the player has guessed the entire word
    if set(word_letters) == set(guessed_letters):
        print("Congratulations! You've guessed the word:", word_to_guess)
        break

# End of the game
if attempts == 0:
    print("Sorry, you've run out of attempts. The word was:", word_to_guess)

print("Thanks for playing!")