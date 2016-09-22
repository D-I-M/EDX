# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 22:42:49 2016

@author: DIM
"""

def isWordGuessed(secretWord, lettersGuessed):

    ls=[]    
    for i in range(len(secretWord)):
        ls.append(secretWord[i])
    ls=set(ls)
    return ls.issubset(lettersGuessed)