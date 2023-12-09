import re

PATH = "C:\\Users\\pierp\\Documents\\Code\\adventofcode\\2023\\Pierre\\"
input = open(PATH+"d05a_input.txt", "r")

sum = 0
SEEDS = [1848591090,462385043,2611025720,154883670,1508373603,11536371,3692308424,16905163,1203540561,280364121,3755585679,337861951,93589727,738327409,3421539474,257441906,3119409201,243224070,50985980,7961058]
N_SEED_RANGES = len(SEEDS)
tmp = []
for i in range(N_SEED_RANGES//2):
    tmp.append([SEEDS[2*i], SEEDS[2*i+1]])

currentStep = tmp
nextStep = []

def convertRangeWithMap(mylist, dest, source, span):
    [a, b] = mylist 

    # Legende des commentaires : 
    # ... = caracteres pas dans le range
    # OOO = caracteres dans le range qui matchent avec cette ligne de la map
    # XXX = caracteres dans le range qui ne matchent pas avec cette ligne de la map
    
    # Cas probablement fusionnable avec des >= mais flemme de reflechir
    if a == source:
        if a+b <= source+span:          #...OOO....
            return [dest, b], []
        else:                           #...OOOXXX...
            return [dest, span], [[a+span, b-span]]
    
    elif a < source:
        if a+b < source:                #...XXX...
            return None, [[a, b]]
        elif a+b > source+span:         #...XXXOOOXXX...
            return [dest, span], [[a, source-a], [source+span, b-span-(source-a)]]
        else:                          #...XXXOOO...
            return [dest, b-(source-a)], [[a, source-a]]
        
    else:
        if source+span < a:             #...XXX...
            return None, [[a, b]]
        elif source+span > a+b:         #...OOO...
            return [dest+(a-source), b], []
        else:                           #...OOOXXX...
            return [dest+(a-source), span-(a-source)], [[source+span, b-(span-(a-source))]]


for line in input.readlines():
    change = re.search(r"^(?P<dest>\d+) (?P<source>\d+) (?P<span>\d+)$", line)
    newmap = re.search(r"map", line)
    
    if newmap != None:
        for rangeNotConverted in currentStep:
            nextStep.append(rangeNotConverted) # numbers not in map stay the same
        currentStep = nextStep
        nextStep = []

    if change == None:
        continue

    dest, source, span = int(change.group("dest")), int(change.group("source")), int(change.group("span"))
    newCurrentStep = []
    for inputRange in currentStep:
        outputRangeConverted, outputRangeNotConverted = convertRangeWithMap(inputRange, dest, source, span)

        if outputRangeConverted != None:
            nextStep.append(outputRangeConverted)

        for rangeNotConverted in outputRangeNotConverted:
            newCurrentStep.append(rangeNotConverted)
    currentStep = newCurrentStep # only keep not yet converted ranges for the rest of this map

for rangeNotConverted in currentStep:
    nextStep.append(rangeNotConverted) # numbers not in map stay the same
currentStep = nextStep

startingNumbers = [currentStep[i][0] for i in range(len(currentStep))]
print(min(startingNumbers))