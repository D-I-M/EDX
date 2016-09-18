# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 22:42:49 2016

@author: DIM
"""

def isWordGuessed(secretWord, lettersGuessed):
    
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
    print(res)