#####################################
#                                   #
# HANGMAN                           #
#                                   #
# author: Isaac and Josh Gormley    #
# date: 2/14/2016                   #
#                                   #
#####################################

import random, sys, os


word = ""
correctLettersGuessed = []
wrongLettersGuessed = []

# function that starts the game
def startGame():
    global word, correctLettersGuessed, wrongLettersGuessed

    # pick a word
    word = getRandomWord()

    # clear out the previous wrongLettersGuessed variable
    correctLettersGuessed = []
    wrongLettersGuessed = []

    #draw the blank board
    drawBoard()

    # take a turn
    takeATurn()


# select a word from the list at random
def getRandomWord():
    words = ["python", "fox", "deer", "wolf", "owl", "dog", "cat", "shrimp", "chimpanzee", "monkey", "lizard", "sparrow", "robin" , "cardinal" , "buffalo" , "squirrel" , "bison" , "rat" , "lion" , "cyclop" , "swallow"]
    randomWord = random.choice(words)
    return randomWord


# gets a letter from the user and validates it
def getLetterFromUser():
    global word, correctLettersGuessed, wrongLettersGuessed
    
    letter = raw_input("pick a letter: ")

    # check that the user entered a single letter
    if len(letter) != 1:
        print "please enter a single letter"
        return getLetterFromUser()
    
    # check that the input is a letter (do not allows spaces, tabs, special characters, numbers, etc)
    if (ord(letter) < 97 or ord(letter) > 122) and (ord(letter) < 65 or ord(letter) > 90):
        print "please enter a letter"
        return getLetterFromUser()

    # now that we know we have a letter, we can lowercase it
    letter = letter.lower()

    # check that the letter has not already been guessed
    if letter in correctLettersGuessed or letter in wrongLettersGuessed:
        print "you have already guessed '%s'" % letter
        return getLetterFromUser()
    
    return letter


def drawBoard():
    # clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')
    # this line (^) is the same as these four lines (v)
        #if os.name == 'nt':
        #    os.system('cls')
        #else:
        #    os.system('clear')

    # draw the board
    print "??????????????????????"
    print ""
    letterBoard = ""
    for letter in word:
        if letter in correctLettersGuessed:
            letterBoard += letter
        else:
            letterBoard += "_"
    print "letterboard: %s" % letterBoard
    #print "correct letters %s" % correctLettersGuessed
    print "incorrect letters %s" % wrongLettersGuessed
    print ""
    print "??????????????????????"


def takeATurn():
    global word, correctLettersGuessed, wrongLettersGuessed

    thisGuess = getLetterFromUser()

    # check if this Guess is in the word
    if thisGuess in word:
        print "you found a letter!"
        # add this letter to the correctLettersGuessed array
        correctLettersGuessed.append(thisGuess)
    else:
        print "oh no, not looking good for you"
        # add this letter to the wrongLettersGuessed array
        wrongLettersGuessed.append(thisGuess)

    # draw the game board
    drawBoard()

    # check if win or lose
    # if the user has made 6 incorrect guesses, they lose
    if len(wrongLettersGuessed) >= 6:
        print ""
        print "YOU LOSE!!!!  The word was %s" % word
        print ""
        sys.exit()

    # if the user has guessed all of the letters, they win
    allCorrect = True
    for letter in word:
        # for this letter in the target word
        if letter not in correctLettersGuessed:
            allCorrect = False
            break

    if allCorrect:
        print ""
        print "WINNER WINNER CHICKEN DINNER"
        print ""
        sys.exit()

    # if we didn't win or lose, take another turn
    takeATurn()

#start the game
startGame()
