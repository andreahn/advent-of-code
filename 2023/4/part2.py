import re

numRegex = r'(\d+)'
totalScore = 0

copies = {}

with open("input.txt", "r") as f:
    lines = f.readlines()

for index, line in enumerate(lines):
    games = line.split(":")[1]
    winningGame = games.split("|")[0]
    acutalGame = games.split("|")[1]

    winningNums = []
    actualNums = []

    for num in re.finditer(numRegex, winningGame):
        winningNums.append(int(num.group()))

    for num in re.finditer(numRegex, acutalGame):
        actualNums.append(int(num.group()))
    
    matches = 0

    for num in actualNums:
        if num in winningNums:
            matches += 1
    
    copiesOfThisCard = copies.get(index)

    if copiesOfThisCard is None:
        copiesOfThisCard = 0
        copies[index] = 1
    else:
        copies[index] = copiesOfThisCard + 1
    
    for i in range(matches):
        currCopyNum = copies.get(int(index) + i + 1)
        
        if currCopyNum is None:
            copies[int(index) + i + 1] = 1 + copiesOfThisCard
        else:
            copies[int(index) + i + 1] = currCopyNum + 1 + copiesOfThisCard


copyTotal = 0

for key, val in copies.items():
    copyTotal += val

print(copyTotal)