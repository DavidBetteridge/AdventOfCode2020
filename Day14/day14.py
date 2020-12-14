import re

def apply_mask(mask, intValue):
    binValue = format(intValue, 'b').zfill(36)
    result = ""
    for i in range(36):
        if mask[i] == 'X':
            result += binValue[i]
        else:
            result += mask[i]

    return int(result,2)

memory = {}
valuePattern = re.compile(r'mem\[(?P<address>[0-9]+)\] = (?P<value>[0-9]+)')
maskPattern = re.compile('mask = (?P<mask>[X01]+)')
for line in open('Day14/day14.txt').read().splitlines():
    if line.startswith("mask"):
        match = maskPattern.match(line)
        mask = match.group("mask")
    else:
        match = valuePattern.match(line)
        address = int(match.group("address"))
        value = int(match.group("value"))
        memory[address] = apply_mask(mask, value)

total = 0
for (address,value) in memory.items():
    total  += value

print(total)
