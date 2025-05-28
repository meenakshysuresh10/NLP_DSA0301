from nltk.corpus import wordnet as wn

nltk.download('wordnet')

word = "bank"
synsets = wn.synsets(word)

print(f"Synsets for '{word}':")
for syn in synsets:
    print(f"{syn.name()}: {syn.definition()}")
    print(f"Examples: {syn.examples()}\n")
