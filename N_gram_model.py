from collections import defaultdict
import random

text = "I love coding. I love Python. I love machine learning."
words = text.split()
bigrams = defaultdict(list)

for i in range(len(words)-1):
    bigrams[words[i]].append(words[i+1])

def generate_text(seed, num_words=5):
    current = seed
    result = [current]
    for _ in range(num_words-1):
        if current not in bigrams:
            break
        next_word = random.choice(bigrams[current])
        result.append(next_word)
        current = next_word
    return ' '.join(result)

print("Generated text:", generate_text("I"))
