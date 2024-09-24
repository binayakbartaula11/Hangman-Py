import random

def hangman():
    # List of possible words
    word_list = ['python', 'java', 'kotlin', 'javascript', 'computer', 'algorithm','binayak','ncit']
    word = random.choice(word_list)
    
    guessed_word = ['_'] * len(word)
    attempts = 10
    guessed_letters = set()

    print("Welcome to Hangman!")

    while attempts > 0:
        print("\nWord to guess: ", ' '.join(guessed_word))
        print(f"Remaining attempts: {attempts}")
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    guessed_word[i] = guess
            print(f"Good guess! '{guess}' is in the word.")
        else:
            attempts -= 1
            print(f"Wrong guess! '{guess}' is not in the word.")

        if '_' not in guessed_word:
            print("\nCongratulations! You've guessed the word:", word)
            break
    else:
        print(f"\nGame over! The word was: {word}")

if __name__ == "__main__":
    hangman()
