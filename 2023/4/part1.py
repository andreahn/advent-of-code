import re

numRegex = r'(\d+)'
totalScore = 0

with open("input.txt", "r") as f:
    lines = f.readlines()

for line in lines:
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

    if matches == 1:
        score = 1
    elif matches > 0:
        score = 1 * 2**(matches-1)
    else:
        score = 0

    totalScore += score

print(totalScore)