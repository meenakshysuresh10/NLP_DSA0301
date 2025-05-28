def pluralize(noun):
    if noun.endswith(('s', 'x', 'z')): return noun + 'es'
    elif noun.endswith('h') and noun[-2] not in 'aeiou': return noun + 'es'
    elif noun.endswith('y') and noun[-2] not in 'aeiou': return noun[:-1] + 'ies'
    else: return noun + 's'

print(pluralize('cat'))   # cats
print(pluralize('bus'))   # buses
print(pluralize('baby'))  # babies
