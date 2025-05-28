import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

text = "NLTK makes natural language processing easy"
tokens = nltk.word_tokenize(text)
tags = nltk.pos_tag(tokens)
print("POS tags:", tags)
