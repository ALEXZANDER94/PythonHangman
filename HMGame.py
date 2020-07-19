import random
import HMWordList
import HangmanForms
from os import system

class HMGame(object):
    """ a game of Hangman """

    def getWordToGuess(self):
        return random.choice(HMWordList.WORDLIST)

    def getHiddenWord(self):
        tempWord = []
        for i in range(len(self.word)):
            tempWord.append('*')
        return tempWord

    def __init__(self):
        self.numberOfGuesses = 0
        self.incorrectGuesses = 0
        self.word = "test" #self.getWordToGuess()
        self.hiddenWord = self.getHiddenWord()
        self.currentGuesses = []

    def updateHiddenWord(self, letter):
        letterInWord = True
        tempWord = []
        for char in self.word:
            tempWord.append(char)
        while(letterInWord):
            index = tempWord.index(letter)
            tempWord[index] = '*'
            self.hiddenWord[index] = letter
            if(letter not in tempWord):
                letterInWord = False

    def checkLetterInWord(self, letter):
        if letter in self.word:
            return True
        else:
            return False

    def checkWordAgainstWord(self, enteredWord):
        if(self.word == enteredWord):
            return True
        else:
            return False

    def checkIfLetterHasBeenGuessed(self, letter):
        if letter in self.currentGuesses:
            return True
        else:
            return False

    def checkIfWordIsGuessed(self):
        tempWord = ""
        for char in self.hiddenWord:
            tempWord += char
        if(tempWord == self.word):
            return True
        else:
            return False

    def startNewGame(self):
        self.numberOfGuesses = 0
        self.incorrectGuesses = 0
        self.word = self.getWordToGuess()
        self.hiddenWord = self.getHiddenWord()
        self.currentGuesses = []
        self.play()

    def showWinningScreen(self):
        system("cls")
        print("Congratulations! You've guessed the word!")
        HangmanForms.HMStage(self.incorrectGuesses)
        print("the word was:\t", self.word)
        keepPlaying = ""
        while(keepPlaying is not "y" or keepPlaying is not "n"):
            keepPlaying = input("Would you like to play again? (y or n) ")
            if(keepPlaying == "y" or keepPlaying == "yes"):
                self.startNewGame()
            elif(keepPlaying == "n" or keepPlaying == "no"):
                quit()
            else:
                print("please enter either yes or no")

    def play(self):
        gameIsWon = False
        status = ""
        
        while(self.incorrectGuesses <= 6 and not gameIsWon):
           
            system("cls")
            if(status == "correct"):
                print(guess, "is in the word")
            elif(status == "incorrect"):
                print(guess, "is not in the word")
            elif(status == "guessed"):
                print("You've already guessed", guess)
            else:
                print(status)
            #show stage
            HangmanForms.HMStage(self.incorrectGuesses)
            if(self.incorrectGuesses is not 6):
                #show the word hidden by asterisks
                print("the word is:\t", end="")
                for item in self.hiddenWord:
                    print(item, end="")
            
                print("\n")

                #show the number of incorrect guesses as well
                print("incorrect guesses:\t", self.incorrectGuesses)

                #show the current guesses
                print("current guesses:\t", end="")
                for item in self.currentGuesses:
                    print(item, end=" ")

                print("\n")
                if(self.checkIfWordIsGuessed()):
                    self.showWinningScreen()

                #ask for guess
                guess = input("Enter your guess: ")

                #check the guess
                if(guess.isalpha()):
                    if(self.checkIfLetterHasBeenGuessed(guess)):
                        status = "guessed"
                        continue
                    self.currentGuesses.append(guess)
                    if(len(guess) > 1): # a word/phrase was entered
                        if(self.checkWordAgainstWord(guess)):
                            self.showWinningScreen()
                        else:
                            status = "incorrect"
                            self.incorrectGuesses += 1

                    elif(len(guess) == 1): # a letter was entered
                        if(self.checkLetterInWord(guess)):
                            status = "correct"
                            self.updateHiddenWord(guess)
                        else:
                            status = "incorrect"
                            self.incorrectGuesses += 1
                    else:
                        print("please enter a valid alphabetic letter or word")
                else:
                    print("please enter a valid alphabetic letter or word")

            else:
                print("the word was:\t", self.word)
                keepPlaying = ""
                while(keepPlaying is not "y" or keepPlaying is not "n"):
                    keepPlaying = input("Would you like to play again? (y or n) ")
                    if(keepPlaying == "y" or keepPlaying == "yes"):
                        self.startNewGame()
                    elif(keepPlaying == "n" or keepPlaying == "no"):
                        quit()
                    else:
                        print("please enter either yes or no")