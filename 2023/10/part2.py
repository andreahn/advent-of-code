import numpy as np
from part1 import *

with open("input.txt", "r") as f:
    lines = f.readlines()

# Good luck making sense of any of the code here....

points = []

passableDiffs = relativeIndexConnectedToPipe

for index, line in enumerate(lines):
    points.append(list(line.strip()))

mapper = np.vectorize(lambda x: '.' if x else 'O')

def findPipesInCycle(lines, startPosition, secondPosition):
    previousPosition = startPosition
    currentPosition = secondPosition
    visitedPositions = [startPosition, secondPosition]

    while True:
        currentPipe = lines[currentPosition[0]][currentPosition[1]]

        if currentPipe == '.':
            break
        elif currentPipe == 'S':
            break
        
        indexForNextPosition = findIndexOfNextPipe(previousPosition, currentPosition, currentPipe)
        previousPosition = currentPosition
        currentPosition = indexForNextPosition
        visitedPositions.append(indexForNextPosition)
    return visitedPositions

def diffInPos(pos1, pos2):
    return (pos1[0] - pos2[0], pos1[1] - pos2[1])

def posIsInTable (pos):
    global matrixHorizontalLength
    global matrixVerticalLength
    if pos[0] >= 0 and pos[0] < matrixVerticalLength:
        if pos[1] >= 0 and pos[1] < matrixHorizontalLength:
            return True
    return False

def isPassable(pos, startPos):
    if pos not in pipesInCycle:
        return True
    else:
        pipe = points[pos[0]][pos[1]]
        possDiff = diffInPos(startPos, pos)
        global positionsThatShouldBeChecked

        # if pipe == '-'

        if possDiff in passableDiffs.get(pipe):
            return False
    return False

startPosition = None

for index, line in enumerate(points):
    try:
        startIndex = line.index('S')
        startPosition = (index, startIndex)
        
        break
    except:
        continue

pipesInCycle = findPipesInCycle(lines, startPosition, newPosition(startPosition, east))

hasEast = newPosition(startPosition, east) in pipesInCycle
hasWest = newPosition(startPosition, west) in pipesInCycle
hasNorth = newPosition(startPosition, north) in pipesInCycle
hasSouth = newPosition(startPosition, south) in pipesInCycle

if hasNorth and hasSouth:
    points[startPosition[0]][startPosition[1]] = '|'
elif hasEast and hasWest:
    points[startPosition[0]][startPosition[1]] = '-'
elif hasNorth and hasEast:
    points[startPosition[0]][startPosition[1]] = 'L'
elif hasNorth and hasWest:
    points[startPosition[0]][startPosition[1]] = 'J'
elif hasSouth and hasWest:
    points[startPosition[0]][startPosition[1]] = '7'
elif hasSouth and hasEast:
    points[startPosition[0]][startPosition[1]] = 'F'


pointsInside = 0

for lineIndex, lineOfPoints in enumerate(points):
    crossingCountForLine = 0
    previousCrossingBorder = None

    for index in range (0, len(lineOfPoints)):
        currentPoint = lineOfPoints[index]
        currentIsBorder = (lineIndex, index) in pipesInCycle
        if (index == len(lineOfPoints) - 1):
            if crossingCountForLine % 2 == 1:
                pointsInside += 1
            continue

        nextPoint = lineOfPoints[index + 1]
        nextIsBorder = (lineIndex, index + 1) in pipesInCycle

        if nextIsBorder:
            if currentIsBorder: # II, --
                moveDirCurrent = (0,1)
                moveDirNext = (0,-1)
                currentContinues = moveDirCurrent in passableDiffs.get(currentPoint)

                if currentContinues and nextPoint == "-": # L- 
                    continue
                elif currentContinues: #LJ 
                    if previousCrossingBorder == "L" and nextPoint == "J":
                        crossingCountForLine += 1
                        previousCrossingBorder = nextPoint
                        
                    elif previousCrossingBorder == "F" and nextPoint == "7":
                        crossingCountForLine += 1
                        previousCrossingBorder = nextPoint
                else: # II 
                        crossingCountForLine += 1
                        previousCrossingBorder = nextPoint

            else: #OI, O7, OL ...
                if crossingCountForLine % 2 == 1:
                    pointsInside += 1
                crossingCountForLine += 1
                previousCrossingBorder = nextPoint
        else:
            if currentIsBorder: # IO
                continue
            else: #OO
                if crossingCountForLine % 2 == 1:
                    pointsInside += 1

    

print("pointsInside: ", pointsInside)