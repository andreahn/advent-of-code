import numpy
with open("input.txt") as f:
    lines = f.readlines()

universe = [[*u.strip()] for u in lines]

def getVerticalLineInUniverse (index, universe):
    return [u[index] for u in universe]

def expandUniverseRows (universe):
    expandedUniverse = []

    for galaxyLine in universe:
        expandedLine = galaxyLine
        
        expandedUniverse.append(expandedLine)

        if "#" not in galaxyLine:
            expandedUniverse.append(expandedLine)
        
    return expandedUniverse

def getGalaxies (universe):
    galaxies = []
    galaxyCount = 0

    for i, universeLine in enumerate(universe):
        for j, spot in enumerate(universeLine):
            if spot == "#":
                galaxyCount += 1
                galaxies.append((i,j))
    
    return galaxies

def distBetweenGalaxies(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])


expandedUniverse = expandUniverseRows(numpy.transpose(universe))
expandedUniverse = expandUniverseRows(numpy.transpose(expandedUniverse))

galaxies = getGalaxies(expandedUniverse)
totalDist = 0

for i, galaxy in enumerate(galaxies):

    for j in range(i + 1, len(galaxies)):
        totalDist += distBetweenGalaxies(galaxies[i], galaxies[j])

print("totalDist part1: ", totalDist)