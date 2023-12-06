import re

maxes = dict()
maxes['r'] = 12
maxes['g'] = 13
maxes['b'] = 14

s = 0

with open("2/input.txt", 'r') as f:
    lines = f.readlines()
    for line in lines:
        ret = re.findall("Game ([0-9]+)", line)
        id = int(ret[0])

        ret = re.findall("([0-9]+) ([rgb])", line)

        s += id
        for n, c in ret:
            if int(n) > maxes[c]:
                s -= id
                break

print(s)
