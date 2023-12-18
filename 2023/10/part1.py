import numpy as np
with open("input.txt", "r") as f:
    lines = f.readlines()

# Good luck making sense of any of the code here....

north = (-1, 0)
east = (0, 1)
west = (0, -1)
south = (1, 0)

relativeIndexConnectedToPipe = {
    '|': [north, south],
    '-': [east, west],
    'L': [north, east],
    'J': [north, west],
    '7': [south, west],
    'F': [south, east]
}

def newPosition(currentPosition, pointToMove):
    return (currentPosition[0] + pointToMove[0], currentPosition[1] + pointToMove[1])

def findIndexOfNextPipe(previousPosition, currentPosition, currentPipe):
    possibleDirections = relativeIndexConnectedToPipe.get(currentPipe)

    for dir in possibleDirections:
        newPos = newPosition(currentPosition, dir)

        if newPos != previousPosition:
            return newPos

def findCycleLength(previousPosition, currentPosition, stepsMade, visitedPositions):

    currentPipe = lines[currentPosition[0]][currentPosition[1]]
    if currentPipe == '.':
        return -1
    elif currentPipe == 'S':
        return stepsMade
    elif currentPosition in visitedPositions:
        return -1
    
    indexForNextPipe = findIndexOfNextPipe(previousPosition, currentPosition, currentPipe)

    return findCycleLength(currentPosition, indexForNextPipe, stepsMade + 1, visitedPositions + [currentPosition])


def findCycleLengthNoRecursion(startPosition, secondPosition):
    previousPosition = startPosition
    currentPosition = secondPosition
    visitedPositions = []
    length = 1

    while True:
        currentPipe = lines[currentPosition[0]][currentPosition[1]]

        if currentPipe == '.':
            length = -1
            break
        elif currentPipe == 'S':
            break
        elif currentPosition in visitedPositions:
            length = -1
            break
        
        indexForNextPosition = findIndexOfNextPipe(previousPosition, currentPosition, currentPipe)
        previousPosition = currentPosition
        currentPosition = indexForNextPosition
        length += 1
    return length

startPosition = None

for index, line in enumerate(lines):
    try:
        startIndex = line.index('S')
        startPosition = (index, startIndex)
        break
    except:
        continue

cycleLengths = []

eastCycleLength = findCycleLengthNoRecursion(startPosition, newPosition(startPosition, east))
cycleLengths.append(eastCycleLength)

southCycleLength = findCycleLengthNoRecursion(startPosition, newPosition(startPosition, south))
cycleLengths.append(southCycleLength)

westCycleLength = findCycleLengthNoRecursion(startPosition, newPosition(startPosition, west))
cycleLengths.append(westCycleLength)

northCycleLength = findCycleLengthNoRecursion(startPosition, newPosition(startPosition, north))
cycleLengths.append(northCycleLength)

print(max(cycleLengths) // 2)
