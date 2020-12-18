def location_of_closing_bracket(line, index):
    openBrackets = 1
    while openBrackets != 0:
        index +=1
        if line[index] == ')':
            openBrackets -= 1
        elif line[index] == '(':
            openBrackets += 1
    return index

def location_of_number_to_left(line, index):
    while line[index] not in ['0','1','2','3','4','5','6','7','8','9']:
        index -= 1
    while index >= 0 and line[index] in ['0','1','2','3','4','5','6','7','8','9']:
        index -= 1    
    return index + 1


def location_of_number_to_right(line, index):
    while line[index] not in ['0','1','2','3','4','5','6','7','8','9']:
        index += 1
    while index < len(line) and line[index] in ['0','1','2','3','4','5','6','7','8','9']:
        index += 1    
    return index - 1

def solve_expression(line):
    expression_without_brackets = ""
    index = 0
    while index < len(line):
        if line[index] == ' ':
            index += 1
        elif line[index] != '(':
            expression_without_brackets += line[index]
            index += 1
        else:
            close = location_of_closing_bracket(line, index)
            expression_without_brackets += solve_expression(line[index+1:close])
            index = close + 1

    # Expression now has no bracket
    plusLocation = expression_without_brackets.find("+")
    while plusLocation != -1:
        lhsLocation = location_of_number_to_left(expression_without_brackets, plusLocation)
        rhsLocation = location_of_number_to_right(expression_without_brackets, plusLocation)
        lhs = expression_without_brackets[lhsLocation:plusLocation]
        rhs = expression_without_brackets[plusLocation+1:rhsLocation+1]
        total = int(lhs) + int(rhs)
        expression_without_brackets = expression_without_brackets[:lhsLocation]+str(total)+expression_without_brackets[rhsLocation+1:]
        plusLocation = expression_without_brackets.find("+")

    return str(eval(expression_without_brackets))

def solve(line):
    return int(solve_expression(line))

print(sum(map(solve, open('Day18/day18.txt').read().splitlines())))