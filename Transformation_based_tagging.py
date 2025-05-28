def apply_transformations(tagged_sentence):
    # Initial tagging (all nouns)
    tagged = [(word, 'NN') for word in tagged_sentence]
    
    # Transformation rules
    for i, (word, tag) in enumerate(tagged):
        if word.lower() in ['is', 'are', 'was']:
            tagged[i] = (word, 'VB')
        elif word.endswith('ly'):
            tagged[i] = (word, 'RB')
        elif word.endswith('ing'):
            tagged[i] = (word, 'VBG')
    return tagged

sentence = "The quickly running dog is barking loudly"
print(apply_transformations(sentence.split()))
