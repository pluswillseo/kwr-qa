import csv
from spellchecker import SpellChecker
import re

# open the CSV file and read the keywords
with open('keywords.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    keywords = [row for row in reader]

# initialize the spell checker
spell_checker = SpellChecker()

# define a regular expression to match any special characters
regex = r'[^A-Za-z0-9 ]'

# define a list of words to ignore (e.g. brand names, product names, etc.)
ignore_list = ["nuptse", "gilet", "adidas","allsaints", "zavetti", "alessandro","dalby", "barbour",
                "shacket","longline","berghaus","women's","men's", "shearling", "bodywarmer", "boohoo",
                "borg", "calvin", "klein","camo", "canada","dkny", "chi", "ugg","trespass", "hilfiger","ted",
                "superdry","sosandar", "skecher","regatta", "reebok","ralph" , "lauren","radley", "sprayway",
                "pour", "moi", "nike", "millie", "mackintosh", "michelle", "keegan", "sally", "levi","levi's",
                "levis","karen", "millen","couture", "joules", "helly", "hanson", "fatface", "evans", "ellesse",
                "emporio", "armani", "dorothy", "perkins", "craghoppers", "converse", "columnbia", "ck", "gilets",
                "dare2b", "fur-lined", "wolfskin", "coatigan"]

# iterate over the keywords and check for any misspellings or special characters
for keyword in keywords:
    # split the keyword into individual words
    words = keyword[0].split()
    
    # iterate over the words and check for any misspellings or special characters
    for word in words:
        # skip any words that are in the ignore list
        if word in ignore_list:
            continue
        
        if len(spell_checker.unknown([word])) > 0 or re.search(regex, word):
            keyword.append("Potential misspelling")
            break

# open the CSV file and write the updated keywords
with open('output.csv', 'w', newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(keywords)