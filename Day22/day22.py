import re

def read_file():
    pack1 = []
    pack2 = []
    pack = []
    lines = open('Day22/day22.txt').read().splitlines()
    for line in lines:
        if line == "Player 1:":
            pack = pack1
        elif line == "Player 2:":
            pack = pack2
        elif line == "":            
            pass
        else:
            pack.append(int(line))
    return (pack1,pack2)

def score_pack(pack):
    return sum([card * (len(pack) - i) for i, card in enumerate(pack)])


def part_one():
    pack1, pack2 = read_file()
    while len(pack1) > 0 and len(pack2) > 0:
        top1 = pack1[0]
        pack1 = pack1[1:]
        top2 = pack2[0]
        pack2 = pack2[1:]

        if top1 > top2:
            pack1.append(top1)
            pack1.append(top2)
        else:
            pack2.append(top2)
            pack2.append(top1)            

    if len(pack1) > 0:
        return score_pack(pack1)
    else:
        return score_pack(pack2)            

def part_two(pack1, pack2):
    roundNumber = 0

    previousRounds = set()

    while len(pack1) > 0 and len(pack2) > 0:
        roundNumber += 1

        s1 = ''.join(map(str,pack1))
        s2 = ''.join(map(str,pack2))
        key = (s1, s2)
        if key in previousRounds:
            return (pack1,[])
        previousRounds.add(key)

        top1 = pack1[0]
        pack1 = pack1[1:]
        top2 = pack2[0]
        pack2 = pack2[1:]

        player1Won = False
        if len(pack1) >= top1 and len(pack2) >= top2:
            subPack1 = pack1[0:top1]
            subPack2 = pack2[0:top2]
            _, r2 = part_two(subPack1, subPack2)
            player1Won = len(r2) == 0

        elif top1 > top2:
            player1Won = True
        else:
            player1Won = False

        if player1Won:
            pack1.append(top1)
            pack1.append(top2)
        else:
            pack2.append(top2)
            pack2.append(top1)                

        if len(pack1) == 0 or len(pack2) == 0:
            return (pack1, pack2)

# print(part_one())

pack1, pack2 = read_file()
pack1, pack2 = part_two(pack1, pack2)
if len(pack1) > 0:
    print(score_pack(pack1))
else:
    print(score_pack(pack2))