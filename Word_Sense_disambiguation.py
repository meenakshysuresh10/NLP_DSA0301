from nltk.wsd import lesk
from nltk.tokenize import word_tokenize

nltk.download('punkt')

sentence = "I went to the bank to deposit money"
word = "bank"

synset = lesk(word_tokenize(sentence), word)
print(f"Best sense for '{word}': {synset.name()} - {synset.definition()}")
