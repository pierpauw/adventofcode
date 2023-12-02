import re

PATH = "C:\\Users\\pierp\\Documents\\Code\\adventofcode\\2023\\Pierre\\"
input = open(PATH+"d02a_input.txt", "r")

sum = 0

def parseNumber(regex, string):
    res = re.search(regex, string)
    if res:
        return int(res.group("number"))
    else:
        return 0

for line in input.readlines():
    game = int(re.search(r"Game (\d*):", line).group()[5:-1])
    hands = re.findall(r"[\w|\s|,]*[;|red$|green$|blue$]", line)

    minRed, minGreen, minBlue = 0, 0, 0
    for hand in hands:
        r = parseNumber(r"(?P<number>\d*) red", hand)
        g = parseNumber(r"(?P<number>\d*) green", hand)
        b = parseNumber(r"(?P<number>\d*) blue", hand)
        if (r>minRed):
            minRed = r
        if (g>minGreen):
            minGreen = g
        if (b>minBlue):
            minBlue = b

    sum += minRed * minGreen * minBlue

print(sum)