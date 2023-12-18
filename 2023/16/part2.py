from day16 import *

tilesEnergized = []

def findEnergizedTileFromPos(startPos, dir):
    res = [["." for c in l] for l in inputData]
    resetVisitedTiles()

    moveBeam(startPos, dir, res)

    count = countEnergizedTiles(res)

    tilesEnergized.append(count)


x = 0
dir = south
for y in range (0, len(inputData[0])):
    findEnergizedTileFromPos((x,y), dir)

x = len(inputData) - 1
dir = north
for y in range (0, len(inputData[0])):
    findEnergizedTileFromPos((x,y), dir)

y = 0
dir = east
for x in range (0, len(inputData)):
    findEnergizedTileFromPos((x,y), dir)


y = len(inputData[0]) - 1
dir = west
for x in range (0, len(inputData)):
    findEnergizedTileFromPos((x,y), dir)

print(max(tilesEnergized))