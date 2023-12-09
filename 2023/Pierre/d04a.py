import re

PATH = "C:\\Users\\pierp\\Documents\\Code\\adventofcode\\2023\\Pierre\\"
input = open(PATH+"d04input.txt", "r")

sum = 0

for line in input.readlines():
    # print()
    winning = line[10:39].split()
    scratched = line[42:-1].split()
    gain = 0
    for n in scratched:
        if n in winning:
            # print(n)
            if gain==0:
                gain = 1
            else:
                gain *= 2
    sum += gain

print(sum)
    