lines =  open('Day19/day19.txt').read().splitlines()

# Checks 105 12  
# Returns -1 for no match,  otherwise the number of tokens consumed
def check_predicate(predicate, rules, line):
    subRuleNumbers = predicate.split(' ')
    consumed = 0
    for subRuleNumber in subRuleNumbers:
        result = check_rule(subRuleNumber, rules, line[consumed:])
        if result == -1:
            # Rule not valid
            return -1
        else:
            consumed += result    
    return consumed


# Returns -1 for no match,  otherwise the number of tokens consumed
def check_rule(ruleNumber, rules, line):

    # No tokens left
    if line == "":
        return -1

    currentRule = rules[ruleNumber]
    if currentRule == '"a"':
        if line[0] == "a": 
            return 1
        else:
            return -1

    if currentRule == '"b"':
        if line[0] == "b": 
            return 1
        else:
            return -1

    predicates = currentRule.split(' | ')
    for predicate in predicates:
        result = check_predicate(predicate, rules, line)
        if result != -1:
            return result    

    # None of the predicates were valid
    return -1


matches = 0
rules = {}
buildingRules = True
for line in lines:
    if line == '':
        buildingRules = False
    elif buildingRules:
        id, rule = line.split(': ')
        rules[id] = rule
    else:
        result = check_rule('0', rules, line)
        matched = len(line) == result
        if matched == True: 
            matches += 1

print(matches)
