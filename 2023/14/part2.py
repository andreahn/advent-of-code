from day14 import *

totalCycles = 1000000000

cycledTable = data
i = 0
cycleInCache = False

while i < totalCycles and not cycleInCache:
    (cycleInCache, cycledTable) = cycleTable(cycledTable)
    i += 1

lengthOfCycleInCache = getLengthOfCycleInCache(cycledTable)
cyclesNeededToReachCycle = i - lengthOfCycleInCache
cyclesNeeded = cyclesNeededToReachCycle + (totalCycles - cyclesNeededToReachCycle) % lengthOfCycleInCache 

# Start over again
cycledTable = data

for j in range(0, cyclesNeeded):
    (cycleInCache, cycledTable) = cycleTable(cycledTable)

total = findTotalLoadForTable(cycledTable)
print("part 2:",total)