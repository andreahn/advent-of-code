import re
import numpy as np

with open("input.txt") as f:
    fileData = f.read()

data = fileData.split("\n")
cycleCache = {}

def transposeListOfStrings(table):
    transposed = np.array([*zip(*table)])
    transposedTableAsList = [l.tolist() for l in transposed]
    return ["".join(charList) for charList in transposedTableAsList]

def rollTable(table):

    transposedTable = transposeListOfStrings(table)

    for lineIndex, line in enumerate(transposedTable):
        fixedLine = line

        if "#" not in line:
            roundRockCount = line.count("O")
            transposedTable[lineIndex] = "O" * roundRockCount + "." * (len(line) - roundRockCount)
            continue

        findRockIter = re.finditer( '#', line)

        currStartIndex = 0

        for cubeRockMatch in findRockIter:
            currEndIndex = cubeRockMatch.start()

            betweenCubeRocks = line[currStartIndex:currEndIndex]

            roundRockCount = betweenCubeRocks.count("O")

            fixedLine = fixedLine[0:currStartIndex]+ "O" * roundRockCount + "." * (len(betweenCubeRocks) - roundRockCount) + fixedLine[currEndIndex:]

            currStartIndex = cubeRockMatch.end()
        
        if currEndIndex < len(line) - 1:
            remainingStringToCheck = line[currEndIndex + 1:]
            roundRockCount = remainingStringToCheck.count("O")
            fixedLine = fixedLine[0:currEndIndex + 1] + "O" * roundRockCount + "." * (len(line) - roundRockCount - currEndIndex)
            transposedTable[lineIndex] = "O" * roundRockCount + "." * (len(line) - roundRockCount)
            
        transposedTable[lineIndex] = fixedLine
    fixedTable = transposeListOfStrings(transposedTable)
    return fixedTable


def findTotalLoadForTable(table):
    tableLength = len(table)
    total = 0

    for i, line in enumerate(table):
        roundRockCount = line.count("O")
        loadForRocks = tableLength - i
        total += roundRockCount * loadForRocks
    
    return total

def flipTable(table):
    flippedTable = []
    for r in table:
        flippedTable.insert(0, r)
    return flippedTable

def getLengthOfCycleInCache(startingpoint):
    length = 0
    curr = startingpoint

    while True:
        curr = cycleCache.get(str(curr))
        length += 1

        if curr == startingpoint:
            break

    return length

def flipTableToTheRight(tableToFlip):
    splitStrings = np.array([[*s] for s in tableToFlip])
    rotated = np.rot90(splitStrings, axes=(1,0))
    rotatedTableAsList = [l.tolist() for l in rotated]
    return ["".join(charList) for charList in rotatedTableAsList]

def cycleTable(table):
    cachedCycleResult = cycleCache.get(str(table))

    if cachedCycleResult is None:
        #north
        rolledTable = rollTable(table)

        # west
        rolledTable = flipTableToTheRight(rolledTable)
        rolledTable = rollTable(rolledTable)

        # south
        rolledTable = flipTableToTheRight(rolledTable)
        rolledTable = rollTable(rolledTable)

        # east
        rolledTable = flipTableToTheRight(rolledTable)
        rolledTable = rollTable(rolledTable)

        # Flip back to original orientation
        rolledTable = flipTableToTheRight(rolledTable)

        cycleCache[str(table)] = rolledTable
        return (False, rolledTable)
    else:
        return (True, cachedCycleResult)