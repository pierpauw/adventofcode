with open("1/input.txt", 'r') as f:
    s = 0
    for line in f:
        first = None
        last = None
        for c in line:
            if c.isdigit():
                if first is None:
                    first = int(c)
                last = int(c)
        s += first * 10 + last
    print(s)
