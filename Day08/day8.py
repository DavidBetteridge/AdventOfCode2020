commands = []
for command in open('Day08/day8.txt').read().splitlines():
    instruction, operand = command.split(' ')    
    commands.append( (instruction, int(operand)) )

def run_program():
    instructionPointer = 0
    accumulator = 0
    seenCommands = []

    while (not instructionPointer in seenCommands) and instructionPointer < len(commands):
        seenCommands.append(instructionPointer)
        instruction, operand = commands[instructionPointer]

        if instruction == 'nop':
            instructionPointer += 1

        if instruction == 'acc':
            accumulator += operand
            instructionPointer += 1

        if instruction == 'jmp':
            instructionPointer += operand

    infiniteLoop = instructionPointer < len(commands)
    return infiniteLoop, accumulator, seenCommands

def part_one():
    _, accumulator, _ = run_program()
    return accumulator

def part_two():
    _, _, seen = run_program()

    for commandNumber in range(0, len(commands)):
        if commandNumber in seen:
            originalInstruction, operand = commands[commandNumber]
            if (originalInstruction != 'acc'):
                if (originalInstruction == 'nop'):
                    commands[commandNumber] = ('jmp', operand)

                if (originalInstruction == 'jmp'):
                    commands[commandNumber] = ('nop', operand)
            
                infiniteLoop, accumulator, _ = run_program()
                if not infiniteLoop:
                    return accumulator

                commands[commandNumber] = (originalInstruction, operand)