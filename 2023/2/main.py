import re

gameDictionary = {}

with open("input.txt", "r") as f:
    lines = f.readlines()

    for line in lines:
        gameId = re.findall(r'(?:Game )([0-9]+):', line)[0]

        game = line.split(":")[1]

        reds = re.findall(r'([0-9]+)(?: red)', game)
        reds = [int(i) for i in reds]

        maxRed = max(reds)

        blues = re.findall(r'([0-9]+)(?: blue)', game)
        blues = [int(i) for i in blues]

        maxBlue = max(blues)

        greens = re.findall(r'([0-9]+)(?: green)', game)
        greens = [int(i) for i in greens]

        maxGreen = max(greens)

        gameDictionary.update({gameId: {"red": maxRed, "green": maxGreen, "blue": maxBlue}})


idSum = 0
actualRed = 12
actualGreen = 13
actualBlue = 14


powerSum = 0 

for gameId, item in gameDictionary.items():
    powerSum += item.get("red") * item.get("blue") * item.get("green")

    if item.get("red") <= actualRed and item.get("green") <= actualGreen and item.get("blue") <= actualBlue:
        idSum += int(gameId)

print("part 1: ", idSum)
print("part 2: ", powerSum)