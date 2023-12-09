import re

PATH = "C:\\Users\\pierp\\Documents\\Code\\adventofcode\\2023\\Pierre\\"
input = open(PATH+"d04input.txt", "r")

NUMCARDS = 213

# card num = index
gains = [0 for _ in range(NUMCARDS+1)]
quantities = [1 for _ in range(NUMCARDS+1)]
quantities[0] = 0 

cardNum = 0
for line in input.readlines():
    cardNum += 1
    winning = line[10:39].split()
    scratched = line[42:-1].split()
    
    for n in scratched:
        if n in winning:
            gains[cardNum]+=1
    
    for i in range(cardNum+1, cardNum+1+gains[cardNum]):
        # create as much copies as you have this card (original & copies)
        quantities[i] += quantities[cardNum]

print(sum(quantities))