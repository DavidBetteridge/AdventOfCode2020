import re

lines =  open('Day19/day19.txt').read().splitlines()

matches = 0
rules = {}
buildingRules = True
images = []
for line in lines:
    if line == '':
        buildingRules = False
    elif buildingRules:
        id, rule = line.split(': ')
        rules[id] = rule
    else:
        images.append(line)

tidyRules = {}
def tidy_rule(ruleNumber):
    currentRule = rules[ruleNumber]

    if currentRule == '"a"':
        return "a"

    if currentRule == '"b"':
        return "b"

    predicates = currentRule.split(' | ')
    parts = []
    for predicate in predicates:       
        pred = ""
        for subRuleNumbers in predicate.split(' '):
            if not subRuleNumbers in tidyRules:
                tidyRules[subRuleNumbers] = tidy_rule(subRuleNumbers)
            pred += tidyRules[subRuleNumbers]

        if len(pred) > 1:
            pred = '(' + pred + ')'         
        parts.append(pred)            
    rule = '|'.join(parts)

    if len(parts) > 1:
        return '(' + rule + ')'
    else:
        return rule


for rule in rules:
    if rule not in tidyRules:
        tidyRules[rule] = tidy_rule(rule)

rule42 = tidyRules['42']
rule31 = tidyRules['31']
rule8 = f"({rule42})+"
result = 0

for i in range(1, 5):
    rule11 = f"({rule42}){{{i}}}({rule31}){{{i}}}"
    rule0 = '(' + rule8 + ')' + '(' + rule11 + ')'
    pattern = re.compile('^' + rule0 + '$')

    for image in images:
        if pattern.match(image):
            result += 1


print(result)        