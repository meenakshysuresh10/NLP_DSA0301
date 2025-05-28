import re

def parse_fopc(expression):
    pattern = r'([∀∃])([a-z])\s*([A-Z][a-z]*\([a-z](?:,\s*[a-z])*\)|¬?[A-Z][a-z]*)'
    matches = re.findall(pattern, expression)
    
    parsed = []
    for quant, var, pred in matches:
        parsed.append({
            'quantifier': quant,
            'variable': var,
            'predicate': pred
        })
    return parsed

print(parse_fopc("∀x P(x) ∧ ∃y Q(y)"))
