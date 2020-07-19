# a Python Hangman Game
import HMGame
from os import system

#main
#print a welcome message
input("""
                                    Welcome to Python Hangman
                I assume you know the rules, but in case you don't here they are:
                
                1.  Simply enter a single letter at a time and see if you get closer to 
                solving the word. 
                
                2.  If you feel confident, go ahead and try to solve it
                by typing in the word. 
                
                3.  Be sure to watch the man carefully, as to not hang him completely!
                
                                      PRESS ENTER TO START
""")

play = True
game = HMGame.HMGame()
while(play):
    system("cls")
    game.startNewGame()
    keepPlaying = ""
    while(keepPlaying is not "y" or keepPlaying is not "n"):
        keepPlaying = input("Would you like to play again? (y or n) ")
        if(keepPlaying == "y" or keepPlaying == "yes"):
            play = True
        elif(keepPlaying == "n" or keepPlaying == "no"):
            quit()
        else:
            print("please enter either yes or no")

    