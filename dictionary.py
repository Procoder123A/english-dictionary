import json
from difflib import get_close_matches
from tkinter import WORD
data=json.load(open('dictionary.json'))
def translate(Word):
    Word=Word.lower() 
    if Word in data:
        return data[Word]
    elif len(get_close_matches(Word,data.keys()))>0:
        yn=input('did you mean %s instead? enter y for yes and n for no:'% get_close_matches(Word,data.keys())[0])
        yn=yn.lower()
        if yn=='y':
            return data[get_close_matches(Word,data.keys())[0]]
        elif yn=='n':
            return "the word dosent exists please double cheak it "
        else:
            return "we did not understand your entry"
    else:
        return "the word dosent exxits please double cheake it"
Word= input("enter your Word=")                            
output=translate(Word)
if type(output)==list:
    for item in output:
        print(item) 
else:
    print(output)         