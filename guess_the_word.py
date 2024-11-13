import random

# Starting with a function that has a list of words defined. Then using random a word from the list is returned as the chosen word.
def chosenWord():
    words = ["apple", "rock", "boulder", "wealthy", "poverty", "education", "castle", "family", "rhinoceros", "whale", "dollar", "quartz"]
    return random.choice(words)

def guessing_game_start():
    word = chosenWord()
    # 6 chances based on Hangman rules.
    chances = 6
    # Tracks the guessed letters done by the user and will be used to prevent repeat letters.
    guessed_letters = set()
    concealed_word = [letter if letter in guessed_letters else "_" for letter in word]

    print("Welcome to Hangman! You must guess a chosen random word one letter at a time! Good luck.")
    print("Current word: ", " ".join(concealed_word))

guessing_game_start()
