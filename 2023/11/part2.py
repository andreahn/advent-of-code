from part1 import universe, getGalaxies
import numpy

def markVoidsInUniverseRows (universe):
    newUniverse = []

    for i, galaxyLine in enumerate(universe):
        replacedLine = galaxyLine

        if "#" not in galaxyLine:
            replacedLine = numpy.array(["X" for a in galaxyLine])
        
        newUniverse.append(replacedLine)
        
    return newUniverse

def newDistBetweenGalaxies(pos1, pos2, universe, distVoid):
    distance = 0
    (pos1x, pos1y) = pos1
    (pos2x, pos2y) = pos2
    (tempx, tempy) = pos1

    xInc = 1 if pos1x < pos2x else -1
    yInc = 1 if pos1y < pos2y else -1

    while tempx != pos2x:
        tempx += xInc
        distance += 1 if universe[tempx][tempy] != "X" else distVoid
    
    while tempy != pos2y:
        tempy += yInc
        distance += 1 if universe[tempx][tempy] != "X" else distVoid

    return distance

newUniverse = markVoidsInUniverseRows(numpy.transpose(universe))
newUniverse = markVoidsInUniverseRows(numpy.transpose(newUniverse))

galaxies = getGalaxies(newUniverse)
totalDist = 0

for i, galaxy in enumerate(galaxies):

    for j in range(i + 1, len(galaxies)):
        totalDist += newDistBetweenGalaxies(galaxies[i], galaxies[j], newUniverse, 1000000)

print("totalDist part2: ", totalDist)