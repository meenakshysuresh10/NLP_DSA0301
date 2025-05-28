def ends_with_ab(s):
    state = 0
    for c in s:
        if state == 0 and c == 'a': state = 1
        elif state == 1 and c == 'b': state = 2
        elif state == 1: state = 0
        else: state = 0
    return state == 2

print(ends_with_ab('aab'))  # False
print(ends_with_ab('xab'))  # True
print(ends_with_ab('aba'))  # False
