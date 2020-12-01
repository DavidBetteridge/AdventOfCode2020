import re

def part_one():
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


def part_two():

    def apply_mask(mask, intValue):
        binValue = format(intValue, 'b').zfill(36)
        result = ""
        for i in range(36):
            if mask[i] == '0':
                result += binValue[i]
            elif mask[i] == '1':
                result += '1'
            elif mask[i] == 'X':
                result += 'X'                    
            else:
                print("Error")
        return result

    def update(lhs, index, addressString, acc):
        if index == 36:
            acc.append(int(lhs,2))
            return

        if addressString[index] == 'X':
            update(lhs + '0', index + 1, addressString, acc)
            update(lhs + '1', index + 1, addressString, acc)
        else:
            update(lhs + addressString[index], index + 1, addressString, acc)

    def update_memory(addressString, value):
        memoryLocationsToUpdate = []
        update("", 0, addressString, memoryLocationsToUpdate)

        for location in memoryLocationsToUpdate:
            memory[location] = value

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
            modifiedAddress = apply_mask(mask, address)
            update_memory(modifiedAddress, value)


    total = 0
    for (address,value) in memory.items():
        total += value

    print(total)

part_two()            
