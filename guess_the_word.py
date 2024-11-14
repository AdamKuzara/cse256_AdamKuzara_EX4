import random

# Starting with a function that has a list of words defined. Then using random a word from the list is returned as the chosen word.
def chosenWord():
    words = ["apple", "rock", "boulder", "wealthy", "poverty", "education", "castle", "family", "rhinoceros", "whale", "dollar", "quartz"]
    return random.choice(words)

def guessing_game_start():
    word = chosenWord()
    # 6 chances based on Hangman rules.
    chances = 6
    guessed_letters = set()
    # The word is made into a list with each letter not guessed by the user correctly being shown as _.
    concealed_word = [letter if letter in guessed_letters else "_" for letter in word]
    letter_count = len(set(word))

    print("Welcome to Hangman! You must guess a chosen random word one letter at a time! Good luck.")
    print("Current word: ", " ".join(concealed_word)) # Joining will show the list of unknown letters for the user to play off.

    while chances > 0:
        # Lower() is used to avoid problems with case sensitivity.
        user_guess = input("Enter a letter: ").lower()

        if user_guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            # Continue is used to avoid making the user lose their turn/chance since it's a word they already guessed.
            continue

        guessed_letters.add(user_guess)
        # This loop uses enumerate to go through each letter in the word list and gives both the index and letter. If the letter at i's position matches the user's guess then concealed_word is updated.
        # Concealed word is updated to replace _ with the letter at the i position. This works even if two letterss are guessed and filled in at once, like p in Apple or l in dollar.
        if user_guess in word:
            for i, letter in enumerate(word):
                if letter == user_guess:
                    concealed_word[i] = user_guess
            # word.count is used to return the number of times user_guess appears in the word by checking if it's greater than 0.
            # letter_count is decremented when a unique letter is correctly guessed for the first time.
            if word.count(user_guess) > 0:
                letter_count -= 1
            print(f"You're getting warmer. {letter_count} letters remaining.")
            # concealed_word[0].upper is used to capitalize the first letter. I just did it because it looked nicer in the output.
            print("Current word: ", " ".join([concealed_word[0].upper()] + concealed_word[1:]))
        else:
            chances -= 1
            print(f"Incorrect guess. Chances remaining: {chances}")
            print("Current word: ", " ".join([concealed_word[0].upper()] + concealed_word[1:]))
        # This is the win condition.
        if "_" not in concealed_word:
            # Similar to my reasoning with concealed_word[0], but since word outputs the full word instead a list .title() is used to capitalize the first letter.
            print("Amazing job! You've guessed the word:", word.title())
            break
    # This is the lose condition.
    if chances == 0:
        print("Sorry, you've run out of chances. The word was:", word.title())

guessing_game_start()
