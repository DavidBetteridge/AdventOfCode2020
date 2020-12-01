import re

class Line:
    def __init__(self, lower, upper, symbol, password):
        self.lower = lower
        self.upper = upper
        self.symbol = symbol
        self.password = password

pattern = re.compile('(?P<lower>[0-9]+)-(?P<upper>[0-9]+) (?P<symbol>[a-z]): (?P<password>[a-z]+)')
lines = open('Day02/day2.txt').read().splitlines()

def parseLine(str):
    match = pattern.match(str)
    lower = int(match.group("lower"))
    upper = int(match.group("upper"))
    symbol = match.group("symbol")
    password = match.group("password")  

    return Line(lower, upper, symbol, password)

def lineIsValid(str, passwordPolicy):
    line = parseLine(str)
    return passwordPolicy(line)

def passwordPolicyPart1(line):
    occurs = line.password.count(line.symbol)
    return line.lower <= occurs <= line.upper

def passwordPolicyPart2(line):
    if (line.password[line.lower - 1] == line.symbol and line.password[line.upper - 1] != line.symbol):
        return True

    if (line.password[line.lower - 1] != line.symbol and line.password[line.upper - 1] == line.symbol):
        return True

    return False        

def part_one():
    return sum(1 for line in lines if lineIsValid(line, passwordPolicyPart1))

def part_two():
    return sum(1 for line in lines if lineIsValid(line, passwordPolicyPart2))