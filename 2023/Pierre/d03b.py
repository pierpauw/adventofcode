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

# Finalement ca aura servi

for line_index in range(len(grid)):
    for symbol in re.finditer(r"\*", grid[line_index]):
        product = 1
        numberCount = 0
        position = symbol.start()

        linesToInspect = [grid[line_index-1], grid[line_index], grid[line_index+1]]
        for line in linesToInspect:
            for number in re.finditer(r"\d+", line):
                start, end = number.start(), number.end()
                if position >= (start-1) and position <= ((end-1)+1):
                    print(int(number.group()))
                    numberCount += 1
                    product *= int(number.group())
        
        if numberCount >= 2:
            print(product, "\n")
            sum += product

print(sum)
