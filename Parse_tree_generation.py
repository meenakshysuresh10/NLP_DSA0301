import nltk
from nltk import CFG

grammar = CFG.fromstring("""
    S -> NP VP
    VP -> V NP | V
    NP -> Det N | N
    Det -> 'the' | 'a'
    N -> 'cat' | 'dog'
    V -> 'chased' | 'ate'
""")
parser = nltk.ChartParser(grammar)
sentence = "the cat chased a dog".split()
for tree in parser.parse(sentence):
    tree.pretty_print()
    break
