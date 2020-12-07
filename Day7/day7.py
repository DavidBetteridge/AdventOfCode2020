def extract_colour(str):
    clean = str.replace('.','').replace('bags','').replace('bag','').strip()
    if clean == 'no other':
        return (0,'none')
    else:
        quantity = int(clean[0])
        colour = clean[2:]
        return (quantity, colour)

rules = {}
for rule in open('Day7/day7.txt').read().splitlines():
    lhs, rhs = rule.split(' bags contain ')
    allowed = list(map(extract_colour, rhs.split(', ')))
    rules[lhs] = allowed

def bag_can_contain_gold(outer_bag):
    if outer_bag == "none": return False

    for inner in rules[outer_bag]:
        qty, colour = inner
        if (colour == "shiny gold"):
            return True
        elif (bag_can_contain_gold(colour)):
            return True
    return False

def part_one():
    total = 0
    for outer in rules:
        if bag_can_contain_gold(outer):
            total += 1
    print(total)    

def count_inner_bags(outer_bag):
    if outer_bag == "none": return 0

    total = 0
    for inner in rules[outer_bag]:
        qty, colour = inner
        total += qty + (qty * count_inner_bags(colour))
    return total

print(count_inner_bags("shiny gold"))