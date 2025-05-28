import nltk
from nltk import PCFG

grammar = PCFG.fromstring("""
    S -> NP VP [1.0]
    NP -> Det N [0.6] | N [0.4]
    VP -> V NP [0.7] | V [0.3]
    Det -> 'the' [0.8] | 'a' [0.2]
    N -> 'cat' [0.5] | 'dog' [0.5]
    V -> 'chased' [0.6] | 'ate' [0.4]
""")
parser = nltk.ViterbiParser(grammar)
sentence = "the cat chased a dog".split()
for tree in parser.parse(sentence):
    tree.pretty_print()
    print("Probability:", tree.prob())
    break
