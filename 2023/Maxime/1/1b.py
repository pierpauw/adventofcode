digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

with open("input.txt", 'r') as f:
    s = 0
    for line in f:
        first = None
        last = None
        for i in range(len(line)):
            c = line[i]
            if c.isdigit():
                if first is None:
                    first = int(c)
                last = int(c)
            else:
                for j in range(len(digits)):
                    if line[i-len(digits[j]) + 1:i + 1] == digits[j]:
                        if first is None:
                            first = j + 1
                        last = j + 1
                        break
        s += first * 10 + last
    print(s)
