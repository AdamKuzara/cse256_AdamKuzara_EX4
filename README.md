# cse256_AdamKuzara_EX4

Created the list of words already. I realize this game will play out just like Hangman with there being attempts and guessing one word at a time. There will need to be user feedback the whole way through.

Finished the rules. I think this is the point where the game will start, probably with a while loop based on the user's chances/attempts being above 0. I know that the guessed_letter set will be used to prevent repeats, but I'll also need something like a counter to tick down the chances/attempts on a wrong guess, but not repeat guesses for the same letter.

The game is done. I didn't spend too much time writing here and focused on comments in the actual program. I'm honestly pretty happy with how this turned out because last time I wrote a Hangman game program I was never able to solve one bug with the game never completing if your last guess was two of the same letter. So for example if I had do--ar (Dollar) and I guess l for my last letter then it would complete the spelling, but the game never ended. I guess in a way I was able to get some closure by starting fresh and trying to use lists/sets instead of a counter and subtracting the user's guess from the alphabet.
