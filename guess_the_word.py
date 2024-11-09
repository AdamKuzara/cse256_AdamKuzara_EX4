import random

# Starting with a function that has a list of words defined. Then using random a word from the list is returned as the chosen word.
def chosenWord():
    words = ["apple", "rock", "boulder", "wealthy", "poverty", "education", "castle", "family", "rhinoceros", "whale", "dollar", "quartz"]
    return random.choice(words)