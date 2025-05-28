def earley_parse(grammar, start, tokens):
    chart = [set() for _ in range(len(tokens)+1)]
    chart[0].add((start, (), 0))
    
    for i in range(len(tokens)+1):
        while True:
            added = False
            for state in list(chart[i]):
                lhs, rhs, pos = state
                if pos < len(rhs):  # Predict/Scan
                    next_sym = rhs[pos]
                    if next_sym in grammar:
                        for prod in grammar[next_sym]:
                            new_state = (next_sym, prod, 0)
                            if new_state not in chart[i]:
                                chart[i].add(new_state)
                                added = True
                else:  # Complete
                    for st in chart[state[2]]:
                        if st[1] and st[1][0] == lhs and st[2] < len(st[1]):
                            new_state = (st[0], st[1], st[2]+1)
                            if new_state not in chart[i]:
                                chart[i].add(new_state)
                                added = True
            if not added: break
    return any(s[0] == start and s[2] == 0 and not s[1] for s in chart[-1])

grammar = {'S': [['NP', 'VP']], 'NP': [['N']], 'VP': [['V']], 
           'N': ['cat'], 'V': ['ate']}
print(earley_parse(grammar, 'S', 'cat ate'.split()))  # True
