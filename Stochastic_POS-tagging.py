from collections import defaultdict
import random

# Simple training data
training_data = [("I", "PRP"), ("love", "VBP"), ("Python", "NN")]

# Build frequency distribution
fd = defaultdict(lambda: defaultdict(int))
for word, tag in training_data:
    fd[word][tag] += 1

def stochastic_tagger(word):
    if word in fd:
        return max(fd[word].items(), key=lambda x: x[1])[0]
    return "NN"  # Default to noun

print(stochastic_tagger("love"), stochastic_tagger("Python"))
