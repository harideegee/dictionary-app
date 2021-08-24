import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def meaning(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        y_n = input("Did you mean '%s'? y or n: " %get_close_matches(word, data.keys())[0]).lower()
        if y_n == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif y_n == "n":
            return "Sorry. I couldn't locate the word you're looking for."
        else:
            return "Your input wasn't valid."
    else:
        return "Sorry, this word isn't there in the dictionary."

word = input("Enter a word: ")

output = meaning(word)
if type(output) == list:
    n = 0
    for i in output:
        n = n + 1
        if len(output) > 1:
            print(str(n) + ". " +  i)
        else:
            print(i)
else:
    print(output)