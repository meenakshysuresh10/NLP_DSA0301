import re
import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

# 1. Regex pattern matching
text = "The cat sat on the mat. The dog barked."
pattern = r'\b\w{3}\b'  # 3-letter words
matches = re.findall(pattern, text)
print("Regex matches:", matches)
