import re

PATH = "C:\\Users\\pierp\\Documents\\Code\\adventofcode\\2023\\Pierre\\"
input = open(PATH+"d01a_input.txt", "r")

DIGITS = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

sum = 0
for line in input.readlines():
    a_index, b_index = len(line), len(line)

    a_res = re.search(r"^\D*\d", line)
    a_index = a_res.span()[1] - 1
    a = int(a_res.group()[-1])

    b_res = re.search(r"\d\D*$", line)
    b_index = b_res.span()[0]
    b = int(b_res.group()[0])

    for digit in DIGITS:
        a_res = re.search(digit, line)
        if a_res != None and a_res.span()[0] < a_index:
            a_index = a_res.span()[0]
            a = DIGITS.index(digit)
            # print(a, a_index, line)

        b_res = re.search(digit[::-1], line[::-1])
        if b_res != None and (len(line)-1 - b_res.span()[0]) > b_index:
            b_index = len(line)-1 - b_res.span()[0]
            b = DIGITS.index(digit)
            # print(b, b_index, line)

    sum += a*10 + b

print(sum)
