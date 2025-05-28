def parse(grammar, start, tokens):
    def expand(symbol):
        if symbol not in grammar:  # Terminal
            if tokens and tokens[0] == symbol:
                tokens.pop(0)
                return True
            return False
        for production in grammar[symbol]:  # Non-terminal
            if all(expand(s) for s in production):
                return True
        return False
    return expand(start) and not tokens

grammar = {
    'S': [['NP', 'VP']],
    'NP': [['Det', 'N']],
    'VP': [['V', 'NP']],
    'Det': ['the', 'a'],
    'N': ['cat', 'dog'],
    'V': ['chased', 'ate']
}
print(parse(grammar, 'S', 'the cat chased a dog'.split()))  # True
