class Rule:
    def __init__(self, quantity_and_colour):
        self.quantity = int(quantity_and_colour[0])
        self.colour = quantity_and_colour[2:]

def extract_colour(str):
    quantity_and_colour = str.replace('.','').replace('bags','').replace('bag','').strip()
    if quantity_and_colour != 'no other':
        return Rule(quantity_and_colour)

rules = {}
for rule in open('Day07/day7.txt').read().splitlines():
    outer_bag, inner_bags = rule.split(' bags contain ')
    rules[outer_bag] = list(x for x in map(extract_colour, inner_bags.split(', ')) if x != None)

def part_one():
    def bag_can_contain_gold_bag(outer_bag):
        return any([inner.colour == "shiny gold" or bag_can_contain_gold_bag(inner.colour) for inner in rules[outer_bag]])

    return sum([bag_can_contain_gold_bag(outer) for outer in rules])

def part_two():
    def count_inner_bags(outer_bag):
        return sum(map(lambda inner: inner.quantity + (inner.quantity * count_inner_bags(inner.colour)),  rules[outer_bag]))    

    return count_inner_bags("shiny gold")