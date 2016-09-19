# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 00:30:31 2016

@author: DIM
"""

def getGuessedWord(secretWord, lettersGuessed):
    
    res=''
    
    for i in range(len(secretWord)):
        
        if secretWord[i] in lettersGuessed:
            res=res+secretWord[i]
        else:
            res=res+'_'
            
    print(res)