import json
import difflib

data = {}
with open("D:/Python/pyapps/dictionary/data.json", "r") as f:
    data = json.load(f)

def get_close_matches(word):
    matches = difflib.get_close_matches(word, data.keys(), cutoff=0.8)
    print(f"These are the matches '{matches}'")
    return matches

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data: #in case user enters words English
        return data[word.title()]
    elif word.upper() in data: #in case user enters words like NATO
        return data[word.upper()]
    else:
        similar_words = get_close_matches(word)
        if len(similar_words) > 0:
            res = str(input(f"Did you mean {similar_words[0]}? Enter y/n:"))
            if res.lower() == 'y':
                return data[similar_words[0]]
            else:
                return "Word doesn't exist"
        else:
            return "Word doesn't exist"

word = str(input("Enter word:"))
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
