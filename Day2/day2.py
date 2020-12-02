import re

pattern = re.compile('(?P<lower>[0-9]+)-(?P<upper>[0-9]+) (?P<symbol>[a-z]): (?P<password>[a-z]+)')

validPasswords = 0
for line in open('C:/personal/AdventOfCode2020/Day2/day2.txt').read().splitlines():
    match = pattern.match(line)
    lower = int(match.group("lower"))
    upper = int(match.group("upper"))
    symbol = match.group("symbol")
    password = match.group("password")

    occurs = password.count(symbol)
    if (occurs >= lower and occurs <= upper):
        validPasswords = validPasswords + 1

print(validPasswords)        
