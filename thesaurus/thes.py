import json
from difflib import get_close_matches
def get_close_mathes_for_word(word):
    if len(get_close_matches(word,data.keys()))>0:
        userprompt=input("Did you mean %s instead? press Y if yes else press N : " % get_close_matches(word,data.keys())[0])
        userprompt=userprompt.capitalize()
        if userprompt=="Y":
            return "%s" % get_close_matches(word,data.keys())[0]
        elif userprompt=="N":
            return "Sorry, the word does not exist"
        else:
            return "Sorry, we did not understand the word"
    else:
        return "Thank you for using our dictionary"

data = json.load(open("data.json"))
def wordchecker(word):
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.capitalize() in data:
        return data[word.capitalize()]
    else:
        return get_close_mathes_for_word(word)

def means(word):
    word = word.lower()
    words=wordchecker(word)
    print(words)
    print("**************************Thank you for using the dictionary*************************")
   
word = input("Enter a word: ")
means(word)
