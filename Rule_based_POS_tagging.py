import re

def regex_tagger(word):
    if re.match(r'^[A-Z][a-z]+$', word): return 'NNP'
    if re.match(r'ing$', word): return 'VBG'
    if re.match(r'ed$', word): return 'VBD'
    if re.match(r'ly$', word): return 'RB'
    if re.match(r'^\d+$', word): return 'CD'
    return 'NN'

text = "The running dog quickly ate 3 bones"
print([(word, regex_tagger(word)) for word in text.split()])
