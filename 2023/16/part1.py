from day16 import *

part1Res = [["." for c in l] for l in inputData]

moveBeam((0,0), east, part1Res)

print(countEnergizedTiles(part1Res))