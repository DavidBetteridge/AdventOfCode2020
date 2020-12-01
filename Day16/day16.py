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

    def all_fields_are_possible(self, numberOfFields):
        self.possible_fields = list(range(0, numberOfFields))
   

def is_field_invalid(fieldValue, classes):
    return not any(c.field_isvalid(fieldValue) for c in classes)

def is_field_valid(fieldValue, classes):
    return any(c.field_isvalid(fieldValue) for c in classes)

def is_ticket_is_valid(ticket, classes):
    fields = ticket.split(',')
    return all([is_field_valid(int(field), classes) for field in fields ])


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

for ticketClass in classes:
    ticketClass.all_fields_are_possible(len(classes))


def part_one():
    total = 0
    for ticket in nearbyTickets:
        fields = ticket.split(',')
        for f in fields:
            if is_field_invalid(int(f), classes):
                total += int(f)
    return total


validTickets = list([ticket for ticket in nearbyTickets if is_ticket_is_valid(ticket, classes)])


for ticket in validTickets:
    fields = list(map(int, ticket.split(',')))

    for i in range(len(fields)):
        value = fields[i]

        for ticketClass in classes:
            if i in ticketClass.possible_fields:
                if not ticketClass.field_isvalid(value):
                    ticketClass.possible_fields.remove(i)

progress = True
while progress: 
    progress = False
    for ticketClass in classes:
        if len(ticketClass.possible_fields) == 1:
            field = ticketClass.possible_fields[0]
            for ticketClass2 in classes:                 
                if ticketClass.name != ticketClass2.name and field in ticketClass2.possible_fields:            
                        ticketClass2.possible_fields.remove(field)
                        progress = True

result = 1
myTicketFields = list(map(int, myTicket.split(',')))
for ticketClass in classes:                        
    if ticketClass.name.startswith("departure"):
        fieldNumber = ticketClass.possible_fields[0]
        result *= myTicketFields[fieldNumber]
print(result)        
