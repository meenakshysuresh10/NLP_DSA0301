def check_agreement(sentence):
    grammar = {
        'S': lambda np, vp: np[1] == vp[1],  # Number agreement
        'NP': [('Det', 'N')],
        'VP': [('V', 'NP')],
        'Det': {'the': 'sg/pl', 'a': 'sg'},
        'N': {'cat': 'sg', 'cats': 'pl'},
        'V': {'chases': 'sg', 'chase': 'pl'}
    }
    tokens = sentence.lower().split()
    if len(tokens) != 3: return False
    det, n, v = tokens
    return (grammar['Det'].get(det, '').startswith(grammar['N'][n]) and \
           grammar['V'][v] == grammar['N'][n]

print(check_agreement("A cat chases"))  # True
print(check_agreement("A cats chase"))  # False
