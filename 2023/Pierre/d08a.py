PATH = "C:\\Users\\pierp\\Documents\\Code\\adventofcode\\2023\\Pierre\\"
input = open(PATH+"d08input.txt", "r")

INSTR = "LRLRLLRRLRRRLRLRRLRLLRRLRRRLRLRLRLRRLRLLRRRLRRRLLRRLRRLRLRRRLLLRRLRLRLRLRLRLLRRRLRLRRRLRRRLRRRLRRRLRRRLRRRLRRRLRRLRRRLLRLLRRLRRLRRLRRRLLRLRRLRLRLRRLLRLRRRLRRLLRLRLRRRLRRLRRLRRLRLLRLRRRLLLRRRLLLLRRLRRRLLLRRLLRLRLRLLLRRRLLRRRLLLRLRRLLRRRLRRRLRLLRRRLRLRLRLLRRLLRRLRRRLRLRRRLRRLRLRRLRRRR"
N_INSTR = len(INSTR)
SKIP = 2
NODES = []
LINKS = []

for line in input.readlines():
    if SKIP:
        SKIP -= 1
        continue

    NODES.append(line[:3])
    LINKS.append([line[7:10], line[12:15]])

currentNode = "AAA"
step = 0

while currentNode != "ZZZ":
    if INSTR[step%N_INSTR] == 'L':
        turn = 0
    else:
        turn = 1

    print(step, currentNode, turn, LINKS[NODES.index(currentNode)])

    currentNode = LINKS[NODES.index(currentNode)][turn]
    step += 1

print(step)