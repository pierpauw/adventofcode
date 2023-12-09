import re

PATH = "C:\\Users\\pierp\\Documents\\Code\\adventofcode\\2023\\Pierre\\"
input = open(PATH+"d05a_input.txt", "r")

sum = 0
currentStep = [1848591090,462385043,2611025720,154883670,1508373603,11536371,3692308424,16905163,1203540561,280364121,3755585679,337861951,93589727,738327409,3421539474,257441906,3119409201,243224070,50985980,7961058]
nextStep = [s for s in currentStep]
N_SEEDS = len(currentStep)

print(min(currentStep))

for line in input.readlines():
    change = re.search(r"^(?P<dest>\d+) (?P<source>\d+) (?P<span>\d+)$", line)
    newmap = re.search(r"map", line)
    
    if newmap != None:
        currentStep = nextStep
        nextStep = [s for s in currentStep]

    if change == None:
        continue

    dest, source, span = int(change.group("dest")), int(change.group("source")), int(change.group("span"))
    for i in range(N_SEEDS):
        s = currentStep[i]
        if s in range(source, source+span):
            nextStep[i] = dest+(s-source)

print(min(nextStep))