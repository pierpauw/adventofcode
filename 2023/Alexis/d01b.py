digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def get_calib_value(line):
    digit_list = []
    for idx in range(len(line)):
            char = line[idx]
            if char.isnumeric():
                digit_list.append(int(char))
            else :
                for i in range(3, 6): # 3 to 5 letters for a digit
                    if idx <= len(line)-i:
                        substring = line[idx:idx+i]
                        if substring in digits:
                            digit_list.append(digits.index(substring)+1)
            
    return digit_list[0] * 10 + digit_list[-1]

output = 0

with open('2023\Alexis\puzzle_input.txt') as f:
    for line in f.readlines():
        output += get_calib_value(line)

print(output)
