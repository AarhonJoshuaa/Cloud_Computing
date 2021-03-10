# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 13:24:56 2021

@author: Aarhon
"""

from gtts import gTTS 

import os 
def ttos(r):
    mytext = r
     
    language = 'en'
    
    myobj = gTTS(text=mytext, lang=language, slow=False) 
    
    myobj.save("audio.mp3") 
ttos('How you doing')
s='How you doin'