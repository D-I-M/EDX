# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "C:\words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    res=False
    d={}
    for i in range(len(secretWord)):
        
        if secretWord[i] in lettersGuessed:
            d[secretWord[i]]=0
            
            d[secretWord[i]]+=1
            lettersGuessed.remove(secretWord[i])
        else:
            d[secretWord[i]]=0
            
        
    if 0 in d.values():
        res=False
    else: 
        res=True
    return res



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    
    res1=''
    for i in range(len(secretWord)):
        
        if secretWord[i] in lettersGuessed:
            res1=res1+secretWord[i]
        else:
            res1=res1+'_ '
            
    return res1


import string
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    al=string.ascii_lowercase
    if len(lettersGuessed)>0:
        for i in lettersGuessed:
            res=al.replace(i,'')
            al=res
    else:
        res=al
    return res
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    global res1
    
    lettersGuessed=[]
    n=0
    let=''
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is', len(secretWord), 'letters long.')
    while n<8:
        print('You have ', 8-n, 'attempts left')
#        print ('Please pick up a letter: ', getAvailableLetters(lettersGuessed))
        print('Available letters ', getAvailableLetters(lettersGuessed))
        let=input('Please pick up a letter: ')
        if let in lettersGuessed:
            print ('You have picked this letter before, please make another guess')
            print ('Available letters',getAvailableLetters(lettersGuessed))
            let=input('Please pick up a letter: ')                        
             
            
        lettersGuessed.append(let)
        if let in secretWord:
            print ('Good guess!', getGuessedWord(secretWord, lettersGuessed))
            print (lettersGuessed, '111')
            if isWordGuessed(secretWord, lettersGuessed)==True:
                print('Congratulations, You won!')

        else:
            print('Oops,make another attempt', getGuessedWord(secretWord, lettersGuessed))
            print (lettersGuessed, '222')
        n+=1
        
    if n>7:
        print ('Sorry, you have run out of guesses. The word was ', secretWord)





# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
