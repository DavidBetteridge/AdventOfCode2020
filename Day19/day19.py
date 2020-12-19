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

#267 too high

# print(rules)
# print(tidyRules)



# def check_rule(ruleNumber, rules, line):

#     # No tokens left
#     if line == "":
#         return []

#     currentRule = rules[ruleNumber]
#     if currentRule == '"a"':
#         if line[0] == "a": 
#             return ["a"]
#         else:
#             return []

#     if currentRule == '"b"':
#         if line[0] == "b": 
#             return ["b"]
#         else:
#             return []

#     matches = []
#     predicates = currentRule.split(' | ')
#     for predicate in predicates:
#         matches += check_predicate(predicate, rules, line)
#     return matches

# # Returns "" for no match otherwise the tokens consumed
# def check_predicate(predicate, rules, line):
#     subRuleNumbers = predicate.split(' ')
#     consumed = ""
#     for subRuleNumber in subRuleNumbers:
#         result = check_rule(subRuleNumber, rules, line[len(consumed):])
#         if result == "":
#             return ""
#         else:
#             consumed += result    
#     return consumed


# # Returns "" for no match otherwise the tokens consumed
# def check_rule(ruleNumber, rules, line):

#     # No tokens left
#     if line == "":
#         return -1

#     currentRule = rules[ruleNumber]
#     if currentRule == '"a"':
#         if line[0] == "a": 
#             return "a"
#         else:
#             return ""

#     if currentRule == '"b"':
#         if line[0] == "b": 
#             return "b"
#         else:
#             return ""

#     predicates = currentRule.split(' | ')
#     for predicate in predicates:
#         result = check_predicate(predicate, rules, line)
#         if result != "":
#             return result    

#     # None of the predicates were valid
#     return ""


# matches = 0
# rules = {}
# buildingRules = True
# for line in lines:
#     if line == '':
#         buildingRules = False
#     elif buildingRules:
#         id, rule = line.split(': ')
#         rules[id] = rule
#     else:

#         # rules["8"] = "42 | 42 8"    
#         # rules["11"] = "42 31 | 42 11 31"    
#         pass
#         # result = check_rule('0', rules, line)
#         # matched = len(line) == result
#         # print(f'{line} {result}')
#         # if matched == True: 
#         #     matches += 1


# rules = {}
# rules["0"] = "1 | 3"
# rules["1"] = '"a"'
# rules["2"] = '"b"'
# rules["3"] = "1 3 | 3"

# print(check_rule('0', rules, "aa"))


# # print(check_rule('0', rules, "aaaaabbaabaaaaababaa"))

# # 

# #176 too low