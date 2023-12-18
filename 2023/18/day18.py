import re
import numpy as np

with open("input.txt") as f:
    lines = f.readlines()

inputRegex = re.compile("([LRDU]{1}) (\d+) \(#([^\)]+)\)")

instructions = []

for line in lines:
    (dir, steps, hex) = re.search(inputRegex, line).groups()
    steps = int(steps)

    instructions.append({
        'dir': dir,
        'steps': steps,
        'hex': hex
    })

def getPart2Inst (hex):
    dir = numToDir(hex[-1])
    steps = int(hex[:len(hex) - 1], 16)

    return (dir, steps)

def numToDir(num):
    match num:
        case '0':
            return "R"
        case '1':
            return "D"
        case '2':
            return "L"
        case '3':
            return "U"

# ---> Part 1 solution
# For this part I reused some code from day 10, which is not efficient enough for part 2

borderVal = ["L", "J", "7", "|", "-", "F"]
digVal = "#"
emptyVal = " "

north = (-1, 0)
east = (0, 1)
west = (0, -1)
south = (1, 0)

passableDiffs = {
    '|': [north, south],
    '-': [east, west],
    'L': [north, east],
    'J': [north, west],
    '7': [south, west],
    'F': [south, east]
}

resGrid = np.full((1, 1), emptyVal)

def getCornerBorder(prevDir, currDir):
    match (prevDir, currDir):
        case ("L", "U"): return "L"
        case ("R", "U"): return "J"
        case ("L", "D"): return "F"
        case ("R", "D"): return "7"

        case ("U", "L"): return "7"
        case ("U", "R"): return "F"
        case ("D", "L"): return "J"
        case ("D", "R"): return "L"

def addColOrRowIfNeeded(i, j):
    global resGrid
    iOffset = 0
    jOffset = 0

    if i < 0:
        # add row above
        iOffset += 1
        resGrid = np.insert(resGrid, 0, emptyVal, axis=0)

    if i >= len(resGrid):
        # add row below
        resGrid = np.insert(resGrid, len(resGrid), emptyVal, axis=0)

    if j < 0:
        # add col to left
        jOffset += 1
        resGrid = np.insert(resGrid, 0, emptyVal, axis=1)

    if j >= len(resGrid[0]):
        # add col to right
        resGrid = np.insert(resGrid, len(resGrid[0]), emptyVal, axis=1)

    return (iOffset, jOffset)

def digBorderInGrid():
    global resGrid
    currI = 0
    currJ = 0

    prevDir = "U"

    for instr in instructions:
        dir = instr.get("dir")
        steps = instr.get("steps")
        resGrid[currI, currJ] = getCornerBorder(prevDir, dir)

        iOffset = 0
        jOffset = 0

        if dir == "R":
            j = currJ
            for step in range(steps):
                j += 1
                (iOffset, jOffset) = addColOrRowIfNeeded(currI, j)
                currI += iOffset
                j += jOffset
                resGrid[currI, j] = "-"
            currJ = j

        elif dir == "L":
            j = currJ
            for step in range(steps):
                j -= 1
                (iOffset, jOffset) = addColOrRowIfNeeded(currI, j)
                currI += iOffset
                j += jOffset
                resGrid[currI, j] = "-"
            currJ = j

        elif dir == "D":
            i = currI
            for step in range(steps):
                i += 1
                (iOffset, jOffset) = addColOrRowIfNeeded(i, currJ)
                i += iOffset
                currJ += jOffset
                resGrid[i, currJ] = "|"
            currI = i

        elif dir == "U":
            i = currI
            for step in range(steps):
                i -= 1
                (iOffset, jOffset) = addColOrRowIfNeeded(i, currJ)
                i += iOffset
                currJ += jOffset
                resGrid[i, currJ] = "|"
            currI = i
        
        prevDir = dir
    
    resGrid[currI, currJ] = getCornerBorder(prevDir, instructions[0].get("dir"))

def fillLagoon():
    # This code is based on my code from day 10 which doesn't work when the border is on an edge
    # so I'm just adding padding around the border because I don't have time to fix this lol
    addColOrRowIfNeeded(-1, -1)
    addColOrRowIfNeeded(len(resGrid), len(resGrid[0]))

    for lineIndex, line in enumerate(resGrid):
        crossingCountForLine = 0
        previousCrossingBorder = None

        for index in range (0, len(line)):
            currentVal = line[index]
            currentIsBorder = currentVal in borderVal
            if (index == len(line) - 1):
                if crossingCountForLine % 2 == 1:
                    resGrid[lineIndex, index] = digVal
                continue

            nextVal = line[index + 1]
            nextIsBorder = nextVal in borderVal

            if nextIsBorder:
                if currentIsBorder: # II, --
                    moveDirCurrent = (0,1)
                    moveDirNext = (0,-1)
                    currentContinues = moveDirCurrent in passableDiffs.get(currentVal)

                    if currentContinues and nextVal == "-": # L- 
                        continue
                    elif currentContinues: #LJ 
                        if previousCrossingBorder == "L" and nextVal == "J":
                            crossingCountForLine += 1
                            previousCrossingBorder = nextVal
                            
                        elif previousCrossingBorder == "F" and nextVal == "7":
                            crossingCountForLine += 1
                            previousCrossingBorder = nextVal
                    else: # II 
                            crossingCountForLine += 1
                            previousCrossingBorder = nextVal

                else: #OI, O7, OL ...
                    if crossingCountForLine % 2 == 1:
                        resGrid[lineIndex, index] = digVal
                    crossingCountForLine += 1
                    previousCrossingBorder = nextVal
            else:
                if currentIsBorder: # IO
                    continue
                else: #OO
                    if crossingCountForLine % 2 == 1:
                        resGrid[lineIndex, index] = digVal

def totalCubicMeters():
    return np.sum(resGrid != emptyVal)

# <--- Part 1 solution


# Part 2 solution --->
# My solution for part 1 is not efficient enough for part 2
# This is an alternative way to solve (both part 1 and 2) using pick's theorem and the shoelace formula

def getPolygon(isPart2):
    borderPoints = []
    i = 0
    j = 0

    for instr in instructions:
        if isPart2:
            (dir, steps) = getPart2Inst(instr.get("hex"))
        else:
            dir = instr.get("dir")
            steps = instr.get("steps")

        if dir == "R":
            j += steps

        elif dir == "L":
            j -= steps

        elif dir == "D":
            i += steps

        elif dir == "U":
            i -= steps

        borderPoints.append((i, j))
        
    return borderPoints

def circumference(borderPoints):
    res = 0

    for index, pos in enumerate(borderPoints):
        if index == len(borderPoints) - 1:
            nextPos = borderPoints[0]
        else:
            nextPos = borderPoints[index + 1]
        res += abs(pos[0] - nextPos[0]) + abs(pos[1] - nextPos[1])

    return res

def shoelaceFormula(borderPoints):
    area = 0

    for i in range(len(borderPoints)):
        if i == len(borderPoints) - 1:
            (x1, y1) = borderPoints[0]
        else:
            (x1, y1) = borderPoints[i + 1]
        (x0, y0) = borderPoints[i]
        
        area += x0 * y1 - x1 * y0

    return abs(area) / 2

def picksTheorem(polygon, c):
    area = shoelaceFormula(polygon)
    return int(area - (c / 2) + 1)

def fullArea(polygon):
    c = circumference(polygon)
    areaInside = picksTheorem(polygon, c)
    
    return areaInside + c

# <--- Part 2 solution