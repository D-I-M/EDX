# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 00:39:11 2016

@author: DIM
"""
import string
def getAvailableLetters(lettersGuessed):
    al=string.ascii_lowercase
    if len(lettersGuessed)>0:
        for i in lettersGuessed:
            res=al.replace(i,'')
            al=res
    else:
        res=al
    return res
