import re
import numpy
import math
with open("input.txt", "r") as f:
    lines = f.readlines()

nodes = {}
instructions = ""
currNodes = []
startNodes = []
endNodes = []

# This is terrible, I never want to see this code ever again

for index, line in enumerate(lines):

    if index == 0:
        instructions = line.strip()
        continue

    findAllRes = re.findall(r'([A-Z\d]+) = \(([A-Z\d]+), ([A-Z\d]+)\)', line)

    if len(findAllRes) > 0:
        findAllRes = findAllRes[0]
        
        if findAllRes[0][2] == "A":
            startNodes.append(findAllRes[0])
        elif findAllRes[0][2] == "Z":
            endNodes.append(findAllRes[0])
        nodes[findAllRes[0]] = {'L': findAllRes[1], 'R': findAllRes[2]}

startNodesWithData = []


def findStepsToSolutionFromNode(nameOfStartNode):
    global instructions
    global nodes

    stepsMade = 0
    solutions = []
    positionsBeforeInstructions = {}
    currentNodeName = nameOfStartNode
    complete = False
    stepsToCycleStart = 0
    instructionReps = 0

    while complete is False:
        positionsBeforeInstructions[currentNodeName] = {"steps": stepsMade, "instructionReps": instructionReps}

        for step in instructions:
            currentNode = nodes.get(currentNodeName)
            
            if step == "L":
                nextNodeName = currentNode.get("L")
            else:
                nextNodeName = currentNode.get("R")

            if nextNodeName in endNodes:
                solutions.append(stepsMade)
            
            stepsMade += 1
            currentNodeName = nextNodeName

        instructionReps += 1

        if currentNodeName in positionsBeforeInstructions.keys():
            if currentNodeName != nameOfStartNode:
                stepsToCycleStart = positionsBeforeInstructions.get(currentNodeName).get("instructionReps") * len(instructions)
            complete = True
    solutionsAfterCycle = list(filter(lambda k: k > stepsToCycleStart, solutions))
    solutionsAfterCycle = [i - stepsToCycleStart for i in solutionsAfterCycle]
    return {"name": nameOfStartNode, "totalSteps": stepsMade, "solutionsFromStart": solutions, "stepsToCycleStart": stepsToCycleStart, "solutionsFromCycle": solutionsAfterCycle, "cycleLength":stepsMade - stepsToCycleStart}


for startNode in startNodes:
    data = findStepsToSolutionFromNode(startNode)
    startNodesWithData.append(data)


complete = False
steps = 0

allStepsFromCycleWithLength = [{"sol": x.get("solutionsFromCycle")[0], "len": x.get("cycleLength")} for x in startNodesWithData]

allStepsFromCycle = [x.get("sol") for x in allStepsFromCycleWithLength]

allCycleLengths = [x.get("len") for x in allStepsFromCycleWithLength]

maxSteps = max(allStepsFromCycle)
maxLen = max(allCycleLengths)

n = maxSteps

toIncrementWith = maxLen

totalSteps = startNodesWithData[0].get("stepsToCycleStart")


while True:
    foundSol = True

    for solFromCycleWithLength in allStepsFromCycleWithLength:
        sol = solFromCycleWithLength.get("sol")
        length = solFromCycleWithLength.get("len")
        if sol != n % length:
            foundSol = False
            break

    if foundSol:
        totalSteps += n + 1
        break
    n += toIncrementWith

    if n > 14935034899483:
        print("fail")
        totalSteps += n + 1
        break

print(totalSteps)