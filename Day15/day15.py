#input = [0,13,1,16,6,17]
input = [0,3,6]
spoken = [-999]

def last_said(what):
    for i in range(len(spoken) -2, 0, -1):
        if spoken[i] == lastSpoken:
            return i
    return -1

for step in range(1, 30000001):
    if (step-1) < len(input):
        spoken.append(input[step-1])
    else:
        lastSpoken = spoken[-1]       
        said = last_said(lastSpoken) 
        if said == -1:
            spoken.append(0)
        else:
            age = (step - 1) - said
            spoken.append(age)
  
print(spoken[-1])

# lastSpoken = {}
# last = 0

# for step in range(200):
#     if step < len(input):
#         last = input[step]
#     else:
#         if not last in lastSpoken:
#             lastSpoken[last] = step  - 1
#             last = 0
#         else:
#             age = step - lastSpoken[last] - 1
#             lastSpoken[last] = step  - 1
#             last = age
    
#     print(last)
