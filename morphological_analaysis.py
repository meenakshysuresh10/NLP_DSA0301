import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

text = "The cats are jumping"
tokens = nltk.word_tokenize(text)
tags = nltk.pos_tag(tokens)
print("POS tags:", tags) 
# Output: [('The', 'DT'), ('cats', 'NNS'), ('are', 'VBP'), ('jumping', 'VBG')]
