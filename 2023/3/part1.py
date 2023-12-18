import re

charRegex = r'[^\.0-9\w]+'
numRegex = r'(\d+)'

with open("input.txt", "r") as f:
    lines = f.readlines()

sum = 0
for index, line in enumerate(lines):

    lineAbove = lines[index - 1] if index > 0 else None
    lineBelow = lines[index + 1] if index < (len(lines) - 1) else None

    numsIter = re.finditer(numRegex, line)
    for match in numsIter:
        startIndex = match.start()
        endIndex = match.end()
        num = line[startIndex:endIndex]
        inclDiagStartIndex = startIndex - 1 if startIndex > 0 else 0
        inclDiagEndIndex = endIndex + 1
        shouldBeAdded = False


        charBefore = line[startIndex - 1] if startIndex > 0 else None
        charAfter = line[endIndex] if endIndex < (len(line) - 2) else None

        if charBefore is not None and re.search(charRegex, charBefore) is not None:
            shouldBeAdded = True
        if charAfter is not None and re.search(charRegex, charAfter) is not None:
            shouldBeAdded = True
        if lineAbove is not None:
            charsAbove = lineAbove[inclDiagStartIndex:inclDiagEndIndex]

            if re.search(charRegex, charsAbove) is not None:
                shouldBeAdded = True

        if lineBelow is not None:
            
            charsBelow = lineBelow[inclDiagStartIndex:inclDiagEndIndex]
            
            if re.search(charRegex, charsBelow) is not None:
                shouldBeAdded = True
        if shouldBeAdded:
            sum += int(num)

print(sum)