moves = open('Day12/day12.txt').read().splitlines()

def part_one():
    x = 0
    y = 0
    direction = 90

    for move in moves:
        action = move[0]
        amount = int(move[1:])
        if action == 'N':
            y += amount
        elif action == 'S':
            y -= amount        
        elif action == 'E':
            x += amount
        elif action == 'W':
            x -= amount                
        elif action == 'R':
            direction = (direction + amount)  % 360                      
        elif action == 'L':
            direction = direction - amount
            if direction < 0: direction += 360
        elif action == 'F':
            if direction == 0:
                y += amount
            elif direction == 90:            
                x += amount
            elif direction == 180:            
                y -= amount
            elif direction == 270:            
                x -= amount                        
            else:
                print(f"Unknown direction {direction}")
        else:
            print("Unknown action")            

    # print(f"x={x} y={y} direction={direction}")
    return abs(x) + abs(y)

def part_two():
    shipX = 0
    shipY = 0
    waypointX = 10
    waypointY = 1

    for move in moves:
        action = move[0]
        amount = int(move[1:])
        if action == 'N':
            waypointY += amount
        elif action == 'S':
            waypointY -= amount        
        elif action == 'E':
            waypointX += amount
        elif action == 'W':
            waypointX -= amount  

        elif action == 'L':
            while amount > 0:
                waypointX, waypointY = (-waypointY, waypointX)
                amount -= 90
            
        elif action == 'R':
            while amount > 0:
                waypointX, waypointY = (waypointY, -waypointX)
                amount -= 90
                
        elif action == 'F':
            shipX += amount * waypointX
            shipY += amount * waypointY
        else:
            print(f"Unknown action {action}")            

        #print(f"shipX={shipX} shipY={shipY} waypointX={waypointX} waypointY={waypointY}")
    return abs(shipX) + abs(shipY)