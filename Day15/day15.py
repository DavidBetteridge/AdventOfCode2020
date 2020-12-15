# #input = [0,13,1,16,6,17]
# input = [0,3,6]
# spoken = [-999]

# def last_said(what):
#     for i in range(len(spoken) -2, 0, -1):
#         if spoken[i] == lastSpoken:
#             return i
#     return -1

# for step in range(1, 30000001):
#     if (step-1) < len(input):
#         spoken.append(input[step-1])
#     else:
#         lastSpoken = spoken[-1]       
#         said = last_said(lastSpoken) 
#         if said == -1:
#             spoken.append(0)
#         else:
#             age = (step - 1) - said
#             spoken.append(age)
  
# print(spoken[-1])

# #234


#dictionary of word against last said
lastSpoken = {}
input = [0,13,1,16,6,17]
#input = [0,3,6]

for i in range(len(input)):
    lastSpoken[input[i]] = i + 1

age = None
last = ""
for step in range(len(input) + 1, 30000001):

    if age == None:
        output = 0
    else:
        output = age

    if output in lastSpoken:
        age = step - lastSpoken[output]
    else:
        age = None
    
    lastSpoken[output] = step
    last = output

print(last)
