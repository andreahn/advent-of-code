import re

with open("input.txt", "r") as f:
    lines = f.readlines()

gearRegex = r'\*{1}'
numRegex = r'(\d+)'
sum = 0

for index, line in enumerate(lines):

    lineAbove = lines[index - 1] if index > 0 else None
    lineBelow = lines[index + 1] if index < (len(lines) - 1) else None

    gearIter = re.finditer(gearRegex, line)

    for gear in gearIter:
        gearIndex = gear.start()
        inclDiagStartIndex = gearIndex - 1 if gearIndex > 0 else 0
        inclDiagEndIndex = gearIndex + 2 if gearIndex < len(line) else gearIndex # TODO: mulig feil?

        numsAdjacent = []

        charsBefore = line[0:gearIndex].split("*")[-1]
        charsAfter = line[gearIndex + 1:].split("*")[0]

        if lineAbove is not None:
            charsAboveRelativeStartIndex = len(lineAbove[0:inclDiagStartIndex].split("*")[-1])
            charsAboveRelativeEndIndex = charsAboveRelativeStartIndex + 3
            charsAbove = lineAbove[0:inclDiagStartIndex].split("*")[-1] + lineAbove[inclDiagStartIndex:inclDiagEndIndex] + lineAbove[inclDiagEndIndex:].split("*")[0]

        if lineBelow is not None:
            charsBelowRelativeStartIndex = len(lineBelow[0:inclDiagStartIndex].split("*")[-1])
            charsBelowRelativeEndIndex = charsBelowRelativeStartIndex + 3
            charsBelow = lineBelow[0:inclDiagStartIndex].split("*")[-1] + lineBelow[inclDiagStartIndex:inclDiagEndIndex] + lineBelow[inclDiagEndIndex:].split("*")[0]

        # Find before

        beforeIter = re.finditer(numRegex, charsBefore)
        
        for num in beforeIter:
            if num.end() == len(charsBefore):
                numsAdjacent.append(num.group())
        

        # Find after

        afterIter = re.finditer(numRegex, charsAfter)

        for num in afterIter:
            if num.start() == 0:
                numsAdjacent.append(num.group())


        # Find above

        if lineAbove is not None:

            aboveIter = re.finditer(numRegex, charsAbove)

            for num in aboveIter:
                if num.start() > charsAboveRelativeStartIndex and num.start() < charsAboveRelativeEndIndex:
                    numsAdjacent.append(num.group())
                elif num.end() > charsAboveRelativeStartIndex and num.end() < charsAboveRelativeEndIndex:
                    numsAdjacent.append(num.group())
                elif num.start() <= charsAboveRelativeStartIndex and num.end() >= charsAboveRelativeEndIndex:
                    numsAdjacent.append(num.group())


        # Find below
        if lineBelow is not None:
            belowIter = re.finditer(numRegex, charsBelow)

            for num in belowIter:
                if num.start() > charsBelowRelativeStartIndex and num.start() < charsBelowRelativeEndIndex:
                    numsAdjacent.append(num.group())
                elif num.end() > charsBelowRelativeStartIndex and num.end() < charsBelowRelativeEndIndex:
                    numsAdjacent.append(num.group())
                elif num.start() <= charsBelowRelativeStartIndex and num.end() >= charsBelowRelativeEndIndex:
                    numsAdjacent.append(num.group())

        if (len(numsAdjacent) == 2):
            sum += int(numsAdjacent[0]) * int(numsAdjacent[1])

print(sum)
