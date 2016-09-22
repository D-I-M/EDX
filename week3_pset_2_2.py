# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 00:30:31 2016

@author: DIM
"""

def getGuessedWord(secretWord, lettersGuessed):
    
    for i in secretWord:
        if i not in lettersGuessed:
            secretWord=secretWord.replace(i,'_')
    return secretWord