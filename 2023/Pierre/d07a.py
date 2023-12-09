import re

PATH = "C:\\Users\\pierp\\Documents\\Code\\adventofcode\\2023\\Pierre\\"
input = open(PATH+"d07input.txt", "r")

HANDS = []
BETS = []

for line in input.readlines():
    HANDS.append(line[:5])
    BETS.append(int(line[6:]))

N = len(HANDS)
strengths = [0 for i in range(N)]

CARDS = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

TYPEMULT = int(1e10)
POKERHANDS = {}
POKERHANDS["5 of a kind"]   = 70 * TYPEMULT
POKERHANDS["4 of a kind"]   = 60 * TYPEMULT
POKERHANDS["Full house"]    = 50 * TYPEMULT
POKERHANDS["3 of a kind"]   = 40 * TYPEMULT
POKERHANDS["2 pairs"]       = 30 * TYPEMULT
POKERHANDS["1 pair"]        = 20 * TYPEMULT
POKERHANDS["High card"]     = 10 * TYPEMULT

TIEBREAKS = [int(1e8), int(1e6), int(1e4), int(1e2), int(1e0)]

for i in range(N):
    cardCount = [0 for card in CARDS]
    tiebreak = 0
    for c in range(5):
        card = HANDS[i][c]
        j = CARDS.index(card)
        cardCount[j] += 1
        tiebreak += (j+2) * TIEBREAKS[c]
    
    if   5 in cardCount:
        strengths[i] = POKERHANDS['5 of a kind'] 
    elif 4 in cardCount:
        strengths[i] = POKERHANDS['4 of a kind']
    elif 3 in cardCount and 2 in cardCount:
        strengths[i] = POKERHANDS['Full house']
    elif 3 in cardCount:
        strengths[i] = POKERHANDS['3 of a kind']
    elif cardCount.count(2) == 2:
        strengths[i] = POKERHANDS['2 pairs']
    elif 2 in cardCount:
        strengths[i] = POKERHANDS['1 pair']
    else:
        strengths[i] = POKERHANDS['High card']
        
    strengths[i] += tiebreak

orderedBets = [bet for strength, bet in sorted(zip(strengths, BETS))]

winnings = 0
for i in range(N):
    winnings += (i+1)*orderedBets[i]

print(winnings)


    
