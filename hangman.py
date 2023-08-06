import random

def choose_word():
    word_list = ["apple","banana", "cherry", "dog","cat","elephant"]
    return random.choice(word_list)

def display(word, guesses):
    display_word = ""
    for letter in word:
        if letter in guesses:
            display_word += letter
        else:
            display_word += "_"
    return display_word

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6 

    print("Welcome to Hangman!")

    while attempts > 0:
        print(display(word, guessed_letters))
        guess = input("Guess a letter:").lower()

        if len(guess) !=1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("correct!")
            if display(word, guessed_letters) == word:
                print("Congratulations, you've won! The word was:", word)
                break
        else:
            attempts -= 1
            print("Incorrect. You have", attempts, "attempts left.")

    if attempts == 0:
        print("sorry,You're dumb. The word was:", word)
    
hangman()