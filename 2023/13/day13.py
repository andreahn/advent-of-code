with open("input.txt") as f:
    fileData = f.read()

lines = fileData.split("\n")

patterns = []
currentPattern = []

for line in lines:
    if line == "":
        patterns.append(currentPattern)
        currentPattern = []
    else:
        currentPattern.append(line)
patterns.append(currentPattern)

def diffsForStringWithPos (str1, str2):
    diffSum = 0
    pos = []

    for i , ch in enumerate(str1):
        if ch != str2[i]:
            diffSum += 1
            pos.append(i)
            if diffSum > 2:
                break
    
    return (diffSum, pos)


def findSmudgeThatCreatesNewRowReflection(pattern, indexToIgnore = -1):
    patternLength = len(pattern)
    isMirror = False
    smudgeHasBeenFixed = False
    smudgePos = (-1, -1)

    for index in range(0, patternLength - 1):
        if index == indexToIgnore:
            continue

        isMirror = True
        smudgeHasBeenFixed = False
        i = index
        j = index + 1

        while i >= 0 and j < len(pattern):
            line1 = pattern[i]
            line2 = pattern[j]
            
            lineDiff, diffIndexes = diffsForStringWithPos(line1, line2)

            if lineDiff == 1 and not smudgeHasBeenFixed:
                lineDiff = 0
                smudgeHasBeenFixed = True
                smudgePos = (i, diffIndexes[0])

            if lineDiff > 0:
                isMirror = False
                break

            i -= 1
            j += 1

        if isMirror and smudgeHasBeenFixed:
            break

    return (smudgeHasBeenFixed, smudgePos)

def findSmudgeThatCreatesNewColumnReflection(pattern, indexToIgnore = -1):
    transposedPattern = [*zip(*pattern)]
    (smudgeHasBeenFixed, smudgePos) = findSmudgeThatCreatesNewRowReflection(transposedPattern, indexToIgnore)

    return (smudgeHasBeenFixed, (smudgePos[1], smudgePos[0]))


def findRowReflection(pattern, indexToIgnore = -1):
    patternLength = len(pattern)
    isMirror = False

    for index in range(0, patternLength - 1):
        if indexToIgnore == index:
            continue
        firstLine = pattern[index]
        secondLine = pattern[index + 1]

        if firstLine == secondLine:
            isMirror = True
            i = index - 1
            j = index + 2

            while i >= 0 and j < len(pattern):
                if pattern[i] != pattern[j]:
                    isMirror = False
                    break
                i -= 1
                j += 1
            
            if isMirror:
                break

    if not isMirror:
        return -1
    return index + 1


def findColumnReflection(pattern, indexToIgnore  = -1):
    transposedPattern = [*zip(*pattern)]
    res = findRowReflection(transposedPattern, indexToIgnore)

    return res
