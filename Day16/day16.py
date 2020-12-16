class ClassRange:
    def __init__(self, text):
        self.lower, self.upper = map(int, text.split('-'))

    def __repr__(self):
        return f'Between {self.lower} and {self.upper}'   

    def field_isvalid(self, fieldValue):
        return self.lower <= fieldValue <= self.upper

class TicketClass:
    def __init__(self, line):
        self.name, range = line.split(': ')
        self.range1, self.range2 = map(ClassRange, range.split(' or '))

    def __repr__(self):
        return f'{self.name} is {self.range1} or {self.range2}'  

    def field_isvalid(self, fieldValue):
        return self.range1.field_isvalid(fieldValue) or  self.range2.field_isvalid(fieldValue)       


def is_field_invalid(fieldValue, classes):
    return not any(c.field_isvalid(fieldValue) for c in classes)


state = "class"
classes = []
myTicket = ""
nearbyTickets = []
for line in open('Day16/day16.txt').read().splitlines():
    if line == "":
        if state == "class":
            state = "your ticket"
        elif state == "your ticket":
            state = "nearby"        
    else:
        if state == "class":
            classes.append(TicketClass(line))
        elif state == "your ticket":
            if line != "your ticket:":
                myTicket = line
        else:
            if line != "nearby tickets:":
                nearbyTickets.append(line)

total = 0
for ticket in nearbyTickets:
    fields = ticket.split(',')
    for f in fields:
        if is_field_invalid(int(f), classes):
            total += int(f)
print(total)            

