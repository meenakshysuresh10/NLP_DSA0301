from nltk.stem import PorterStemmer

stemmer = PorterStemmer()
words = ["running", "jumps", "happiness", "fairly"]
stems = [stemmer.stem(word) for word in words]
print("Stems:", stems)  
# Output: ['run', 'jump', 'happi', 'fairli']
