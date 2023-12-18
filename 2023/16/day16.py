with open("input.txt") as f:
    lines = f.readlines()

inputData = [[*l.strip()] for l in lines]

north = (-1, 0)
east = (0, 1)
west = (0, -1)
south = (1, 0)

mirrors = {
    '\\': {
        north: [west],
        east: [south],
        south: [east],
        west: [north]
    },
    '/': {
        north: [east],
        east: [north],
        south: [west],
        west: [south]
    },
    '|': {
        north: [north],
        east: [north, south],
        south: [south],
        west: [north, south]
    },
    '-': {
        north: [east,west],
        east: [east],
        south: [east, west],
        west: [west]
    }
}

visitedTiles = {}

def storeVisited(pos, dir):
    visited = visitedTiles.get(pos)
    if visited is None:
        visitedTiles[pos] = [dir]
    else:
        visitedTiles[pos].append(dir)

def hasBeenVisited(pos, dir):
    visited = visitedTiles.get(pos)

    if visited is not None:
        return dir in visited
        
    return False

def resetVisitedTiles():
    global visitedTiles
    visitedTiles = {}

def moveBeam (startPos, dir, resTable):
    currPos = startPos
    currDirection = dir

    while True:
        if currPos[0] not in range(0,len(inputData)) or currPos[1] not in range(0, len(inputData[0])):
            return
        
        tileHasBeenVisited = hasBeenVisited(currPos, currDirection)
        resTable[currPos[0]][currPos[1]] = "#"

        if tileHasBeenVisited:
            return
        else:
            storeVisited(currPos, currDirection)
            currTile = inputData[currPos[0]][currPos[1]]

            if currTile in mirrors.keys():
                nextDirections = mirrors.get(currTile).get(currDirection)

                if len(nextDirections) > 1:
                    moveBeam(currPos, nextDirections[1], resTable)
                currDirection = nextDirections[0]
                currPos = (currPos[0] + currDirection[0], currPos[1] + currDirection[1])
            else:
                currPos = (currPos[0] + currDirection[0], currPos[1] + currDirection[1])

def countEnergizedTiles(table):
    sum = 0
    for l in table:
        sum += l.count("#")

    return sum
