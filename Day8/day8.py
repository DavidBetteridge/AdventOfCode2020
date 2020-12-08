instructionPointer = 0
accumulator = 0
seenCommands = []
commands = []
for command in open('Day8/day8.txt').read().splitlines():
    instruction, operand = command.split(' ')    
    commands.append( (instruction, int(operand)) )


while not instructionPointer in seenCommands:
    seenCommands.append(instructionPointer)
    instruction, operand = commands[instructionPointer]

    if instruction == 'nop':
        instructionPointer += 1

    if instruction == 'acc':
        accumulator += operand
        instructionPointer += 1

    if instruction == 'jmp':
        instructionPointer += operand


print(accumulator)