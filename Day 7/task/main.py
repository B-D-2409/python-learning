import random
from hangman_words import word_list
from hangman_art import stages,logo
print(logo)

# TODO-1: Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Create variables
lives = 6
game_over = False
correct_letters = []
display = ""

# Create initial placeholder
for _ in range(word_length):
    display += "_"
print(display)

# Game loop
while not game_over:
    guess = input("Guess a letter: ").lower()

    # TODO-4: Check if the user has already guessed the letter.
    if guess in correct_letters:
        print(f"You've already guessed '{guess}'. Try another letter.")
        print(display)
        continue

    # Store guessed letter
    correct_letters.append(guess)

    # Create a new display string
    new_display = ""
    for letter in chosen_word:
        if letter in correct_letters:
            new_display += letter
        else:
            new_display += "_"

    # Check guess
    if guess in chosen_word:
        print(f"Good job! '{guess}' is in the word.")
    else:
        # TODO-2: Reduce a life if guess is not in the chosen_word.
        lives -= 1
        print(f"You guessed '{guess}', that's not in the word. You lose a life.")
        print(f"**************************** {lives}/6 LIVES LEFT ****************************")
        if lives == 0:
            game_over = True
            print(stages[lives])
            print(f"\nIT WAS '{chosen_word.upper()}'! YOU LOSE 😢")
            break

    # Update display
    display = new_display
    print(display)

    # TODO-3: Print ASCII art from hangman_art.py
    print(stages[lives])

    # Check if player has won
    if "_" not in display:
        game_over = True
        print("🎉 You win! 🎉")
