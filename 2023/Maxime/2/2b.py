import re

maxes = dict()

s = 0

with open("2/input.txt", 'r') as f:
    lines = f.readlines()
    for line in lines:
        ret = re.findall("([0-9]+) ([rgb])", line)

        maxes['r'] = 0
        maxes['g'] = 0
        maxes['b'] = 0

        for n, c in ret:
            maxes[c] = int(n) if int(n) > maxes[c] else maxes[c]
        
        s += maxes['r'] * maxes['g'] * maxes['b']

print(s)
