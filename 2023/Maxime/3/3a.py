import re

with open("3/input.txt", 'r') as f:
    lines = f.readlines()
    h, w = len(lines), len(lines[0]) - 1
    print(h, w)

    s = 0

    for i in range(h):
        line = lines[i]
        ret = re.finditer("[0-9]+", line)

        for match in ret:
            part = int(match.group())
            span_start, span_end = match.span()

            # left
            if (span_start) > 0 and (line[span_start - 1] != '.'):
                s += part
                continue

            # right
            if (span_end) < w and (line[span_end] != '.'):
                s += part
                continue
            
            for j in range(max(span_start - 1, 0),
                           min(span_end + 1, w - 1)):
                # above
                if (i > 0)\
                    and (lines[i - 1][j] != '.')\
                    and not lines[i - 1][j].isdigit():
                    s += part
                    break
                
                # below
                if (i < h - 1)\
                    and (lines[i + 1][j] != '.')\
                    and not lines[i + 1][j].isdigit():
                    s += part
                    break
            
    print(s)
