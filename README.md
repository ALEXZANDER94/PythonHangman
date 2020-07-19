# PythonHangman
A game of Hangman made in Python

This is a game of Hangman made in Python. For this game, I decided to use a more object-oriented approach.

The game rules are the same as the traditional game of hangman. There is a wordlist located in the HMWordList.py file; this is a collection of 50 random words so each time a new game
is started, the word is likely not the same, neither in size or in sequence.

The HangmanForms.py just holds a single function that serves to display the actual hangman structure. With each increment of the incorrectGuesses variable, a new part will be added
to the structure until the complete man is shown along with the "Game Over" prompt.

The entire main function is located in the PythonHangman.py file, and does not consist of much other than a Welcome message, class construction, and while loop containing the game
session

The bulk of the program is in the HMGame.py file, which consists of the entire game class definition. In this file is the constructor that initializes all attributes of the game;
from the number of incorrect guesses, to the hidden word (as a list). I had to use a List data Structure for the hiddenWord variable to capitalize on a List Structures mutability.
I had gone with a string at the start, but later found that my functions that allow the HiddenWord to gradually show with each correct guess could not be complete as String are
immutable in Python.

Along with the constructor and the entire gameplay method, there are several other functions that are defined in the class. Quite a few are simple checks to condense the play
function. There is, however, the UpdateHiddenWord method of the class. This method is responsible more making the hiddenWord variable show more of the actual word as the player
guesses right more and more, the tricky part of this method was when there were multiple occurences of the letter in the word; I had to make sure that for each occurence, the
correct index of the hidden word would show for the user.

At the start of the game, the player is show a blank hangman structure along with two messages that show the player the hiddenWord (all asterisks at the start, but at least the 
player gets a sense of how many letters are in the word), the number of incorrect guesses made (0 at the start), and the current guesses the player has made - this is so they won't enter the same letter over and over.

Guesses are handled as follows:
If the letter is in the word - all occurences of the letter will be revealed in the hiddenWord, the current guesses will be updated also
If the letter is not in the word - the hangman structure will change, the incorrect guesses will be incremented, and the current guesses will be updated
If the letter has already been guessed - the player will be notified that the guess has already been made, the structure will not change, and the incorrect guesses will not be
incremented

The Player also has the option to guess the word by typing in the full word. That is, if the player has guessed a couple of letters and thinks they know what the word is, they may
type it in to see if they are correct. If they are incorrect, this will be handled as a single incorrect guess - the hangman structure will change, the incorrect guesses will be incremented, 
and the current guesses will be updated.

When the word is guessed correctly or the player has lost, they will be prompted for a chance to play again. If they choose yes, the game will reset - a new word is chosen,
incorrect guesses are reset to 0, current guesses will be cleared, and the structure will be blank again.
