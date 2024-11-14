import pytest
from guess_the_word import chosenWord, guessing_game_start
# pytest -s test_guess_the_word.py - Saved this up here so I can just copy it into terminal each time.

# First test was something really simple and honestly not even that helpful, but it was more for me testing if I was getting pytest to work. This just checks for a word that doesn't exist on the list.
def chosenWord():
    words = ["apple", "rock", "boulder", "wealthy", "poverty", "education", "castle", "family", "rhinoceros", "whale", "dollar", "quartz"]
    chosen_word = chosenWord()
    assert chosen_word in words, f"You were supposed to get something from {words}, but got {chosen_word} instead."

# I deleted a previous test because it ended up being too frustrating to work with, but this one thankfully actually helped. Sort of, but it was nice actually seeing pytest working.
# This still consistently works as well. However if you make multiple errors it will only output one. I think it's the first error type you make.
def test_invalid_input():
    # Test for invalid input: Non-alphabetical character
    with pytest.raises(ValueError, match="Invalid input. Please enter a single letter."):
        guessing_game_start(user_input="1")  # Invalid input (number instead of letter)

    # Test for invalid input: More than one character
    with pytest.raises(ValueError, match="Invalid input. Please enter a single letter."):
        guessing_game_start(user_input="abc")  # Invalid input (multiple letters)

    # Test for valid input (to check functionality)
    result = guessing_game_start(user_input="a")  # Valid input
    assert result is None  # Expect no exception, game should continue normally
