
# PRECEDENCES = { '^':4, '*':3, '/':3, '+':2, '-':2 }

PRECEDENCES = { '+':2, '*':2 } #Part 1
#PRECEDENCES = { '+':3, '*':2 } #Part 2


ASSOCIATIVITY = { '^':'RIGHT', '*':'LEFT', '/':'LEFT', '+':'LEFT', '-':'LEFT'  }


def higher_precedence(op1, op2):
    return PRECEDENCES[op1] > PRECEDENCES[op2]

def equal_precedence(op1, op2):
    return PRECEDENCES[op1] == PRECEDENCES[op2]

def is_operator(c):
    return c in ['+', '*', '/', '-', '^']

def move_operator(operatorStack, c):
    if len(operatorStack) == 0: return False

    topOperator = operatorStack[-1]
    if topOperator == '(': return False

    return (higher_precedence(topOperator, c) or (equal_precedence(topOperator, c) and ASSOCIATIVITY[topOperator] == 'LEFT'))

def evaluate(line):
    outputQueue = []
    operatorStack = []
    for c in line:
        if c.isdigit():
            outputQueue.append(c)
        elif c == '(':        
            operatorStack.append(c)
        elif c == ')':        
            while len(operatorStack) > 0 and operatorStack[-1] != '(': 
                outputQueue.append(operatorStack.pop())
            if len(operatorStack) > 0 and operatorStack[-1] == '(':   
                operatorStack.pop()          
        elif is_operator(c): 
            while move_operator(operatorStack, c):
                outputQueue.append(operatorStack.pop())
            operatorStack.append(c)

    while len(operatorStack) > 0:        
        outputQueue.append(operatorStack.pop())

    work = []
    for token in outputQueue:
        if not is_operator(token):
            work.append(token)
        else:
            rhs = work.pop()
            lhs = work.pop()
            new = int(eval(f'{lhs} {token} {rhs}'))
            work.append(new)

    return work[0]

print(sum(map(evaluate, open('Day18/day18.txt').read().splitlines())))    