def get_calib_value(line):
    digit_list = []
    for char in line:
            if char.isnumeric():
                digit_list.append(int(char))
    return digit_list[0] * 10 + digit_list[-1]

output = 0

with open('2023\Alexis\puzzle_input.txt') as f:
    for line in f.readlines():
        output += get_calib_value(line)

print(output)
