import re

PATH = "C:\\Users\\pierp\\Documents\\Code\\adventofcode\\2023\\Pierre\\"
input = open(PATH+"d03a_input.txt", "r")

PAD = '.'
# parts = []
sum = 0
grid = []

firstLine = True
for line in input.readlines():
    if firstLine:
        firstLine = False
        paddingLine = PAD * (len(line)-1 + 2)
        grid.append(paddingLine)
    
    grid.append(PAD + line[:-1] + PAD) # -1 car \0

grid.append(paddingLine)

for line_index in range(len(grid)):
    # print(grid[line_index])
    for number in re.finditer(r"\d+", grid[line_index]):
        start, end = number.start(), number.end()

        isSymbolUp = (re.search(r"[^0-9"+PAD+"]", grid[line_index-1][start-1 : end+1]) != None)
        isSymbolDown = (re.search(r"[^0-9"+PAD+"]", grid[line_index+1][start-1 : end+1]) != None)
        isSymbolLeft = (re.search(r"[^0-9"+PAD+"]", grid[line_index][start-1]) != None)
        isSymbolRight = (re.search(r"[^0-9"+PAD+"]", grid[line_index][end]) != None)

        if isSymbolUp or isSymbolDown or isSymbolLeft or isSymbolRight:
            # Ca c'est quand je me suis dit que peut-etre qu'il ne fallait pas compter 2 fois le meme
            # n = int(number.group())
            # if n not in parts:
            #     parts.append(n)
            sum += int(number.group())
            print(int(number.group()), start, end)

# OUIIIIIIIII ca prend tout le nombre et pas que la partie en contact avec le symbole 
# J'avais bien lu puis mal lu puis bien relu derrière bref

# for line_index in range(len(grid)):
#     for symbol in re.finditer(r"[^0-9"+PAD+"]", grid[line_index]):
#         start, end = symbol.start(), symbol.end()

#         charsUp = grid[line_index-1][start-1 : end+1+1]
#         charsDown = grid[line_index+1][start-1 : end+1+1]
#         charsLeft = grid[line_index][start-1]
#         charsRight = grid[line_index][end]
#         adjacent = [charsUp, charsDown, charsLeft, charsRight]

#         for chars in adjacent:
#             for number in re.findall(r"\d+", chars):
#                 sum += int(number)

print(sum)
