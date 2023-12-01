import re

PATH = "C:\\Users\\pierp\\Documents\\Code\\adventofcode\\2023\\Pierre\\"

input = open(PATH+"d01a_input.txt", "r")
endOfFile = False

sum = 0

while not endOfFile:
    line = input.readline()
    if line == "":
        endOfFile = True
    else:
        a = re.search(r"^\D*(\d)", line).group(0)[-1]
        b = re.search(r"(\d)\D*$", line).group(0)[0]
        sum += int(a)*10 + int(b)

print(sum)
