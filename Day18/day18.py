# class N:
#     def __init__(self, num):
#         self.number = num

#     def __radd__(self, other):
#         if isinstance(other, self.__class__):
#             return self.number + other.number
#         else:
#             return self.number + other

#     def __add__(self, other):
#         if isinstance(other, self.__class__):
#             return self.number + other.number
#         else:
#             return self.number + other

#     def __sub__(self, other):
#         if isinstance(other, self.__class__):
#             return self.number * other.number
#         else:
#             return self.number * other

# lines = open('Day18/day18.txt').read().splitlines()

# #line = "1 + (2 * 3) + (4 * (5 + 6))"
# line = "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"

# for i in range(0,10):
#     line = line.replace(str(i), f"N({str(i)})")

# line = line.replace("*", "-")    

# print(eval(line))

def location_of_closing_bracket(line, index):
    index+=1
    openBrackets = 1
    while openBrackets != 0:
        if line[index] == ')':
            openBrackets -= 1
        elif line[index] == '(':
            openBrackets += 1
        index +=1
    return index

def evalulate_line(line):
    
    runningTotal = 0
    index = 0
    operator = ""
    while index < len(line):    
        if line[index] == '(':
            closing = location_of_closing_bracket(line, index)
            nextValue = evalulate_line(line[index+1:closing-1])

            if operator == "":
                runningTotal = nextValue
            elif operator == "+":
                runningTotal += nextValue
            elif operator == "*":
                runningTotal *= nextValue

            index = closing + 1
        elif line[index] == ')':
            print("oh")    
        elif line[index] == '+':
            operator = "+"
            index += 1
        elif line[index] == '*':
            operator = "*"
            index += 1
        elif line[index] == ' ':
            index += 1            
        elif int(line[index]) in [0,1,2,3,4,5,6,7,8,9]:
            if operator == "":
                runningTotal = int(line[index])
            elif operator == "+":
                runningTotal += int(line[index])
            elif operator == "*":
                runningTotal *= int(line[index])        
            index += 1                    

    print(f"{line} = {runningTotal}")
    return runningTotal      

lines = open('Day18/day18.txt').read().splitlines()

result = 0
for line in lines:
     result += evalulate_line(line)
print(result)     




