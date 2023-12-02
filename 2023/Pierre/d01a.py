import re

PATH = "C:\\Users\\pierp\\Documents\\Code\\adventofcode\\2023\\Pierre\\"
input = open(PATH+"d01a_input.txt", "r")

sum = 0

for line in input.readlines():
    a = re.search(r"^\D*(\d)", line).group(0)[-1]
    b = re.search(r"(\d)\D*$", line).group(0)[0]
    sum += int(a)*10 + int(b)

print(sum)
