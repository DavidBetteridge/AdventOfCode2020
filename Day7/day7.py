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

    def worker(inner):
        _, colour = inner
        return colour == "shiny gold" or bag_can_contain_gold(colour) 

    return any([True for inner in rules[outer_bag] if worker(inner)])

def count_inner_bags(outer_bag):
    if outer_bag == "none": return 0

    def worker(inner):
        qty, colour = inner
        return qty + (qty * count_inner_bags(colour))        

    return sum(map(worker,  rules[outer_bag]))

def part_one():
    return sum([1 for outer in rules if bag_can_contain_gold(outer)])

def part_two():
    return count_inner_bags("shiny gold")