import re
with open("input.txt", "r") as f:
    lines = f.readlines()

workflows = {}

parts = []

lineRegex = re.compile("([^{]+){(.*)}")
conditionRegex = re.compile("([a-z]+)([<>]{1})(\d+):(.+)")
partsRegex = re.compile("x=(\d+),m=(\d+),a=(\d+),s=(\d+)")

conditionPassed = "X"

def applyCond(c, part):
    parsedCond = re.search(conditionRegex, c)
    if parsedCond.group(2) == "<":
        return parsedCond.group(4) if part.get(parsedCond.group(1)) < int(parsedCond.group(3)) else conditionPassed
    else:
        return parsedCond.group(4) if part.get(parsedCond.group(1)) > int(parsedCond.group(3)) else conditionPassed

def getPart1Input():
    w = True
    for line in lines:
        line = line.strip()

        if line == "":
            w = False
            continue

        if w:
            s = re.search(lineRegex, line)
            workflowName = s.group(1)
            dataForWorkflow = s.group(2).split(",")

            finalLocation = dataForWorkflow[-1]
            conds = dataForWorkflow[:-1]
            conditions = []

            for c in conds:
                conditions.append({
                    's': c
                })
            
            workflows[workflowName] = {
                'finalLocation': finalLocation,
                'conds': conditions
            }
        else:
            s = re.search(partsRegex, line)
            parts.append({
                'x': int(s.group(1)),
                'm': int(s.group(2)),
                'a': int(s.group(3)),
                's': int(s.group(4))
            })


def getPart2Input():
    for line in lines:
        line = line.strip()

        if line == "":
            break

        s = re.search(lineRegex, line)
        workflowName = s.group(1)
        dataForWorkflow = s.group(2).split(",")

        finalLocation = dataForWorkflow[-1]
        conds = dataForWorkflow[:-1]
        conditions = []
        locations = [finalLocation]

        for c in conds:
            parsedCond = re.search(conditionRegex, c)
            condName = parsedCond.group(1)
            condType = ("max" if parsedCond.group(2) == "<" else "min")
            condVal = int(parsedCond.group(3))
            locations.append(parsedCond.group(4))
            conditions.append({
                's': c,
                condName: {
                    condType: (condVal + 1) if condType == "min" else (condVal - 1)
                },
                'dest': parsedCond.group(4)
            })
            
            workflows[workflowName] = {
                'finalLocation': finalLocation,
                'conds': conditions
            }


def passPartThroughWorkflow (workflow, part):
    for c in workflow.get("conds"):
        res = applyCond(c.get("s"), part)
        
        if res != conditionPassed:
            return res
    if res == conditionPassed:
        res =workflow.get("finalLocation")
    return res

def partIsAccepted(part):
    currWorkflowName = "in"

    while currWorkflowName not in ["A", "R"]:
        currWorkflowName = passPartThroughWorkflow(workflows.get(currWorkflowName), part)
    
    return True if currWorkflowName == "A" else False

def applyConditionToRange(condition, range, inverse=False):
    compatible = True
    if condition is None:
        return (compatible, range)
    
    fixedRange = range

    if condition.get("x") is not None:
        varName = "x"
        rangeIndex = 0

    elif condition.get("m") is not None:
        varName = "m"
        rangeIndex = 1

    elif condition.get("a") is not None:
        varName = "a"
        rangeIndex = 2

    else:
        varName = "s"
        rangeIndex = 3

    if not inverse:
        maxVal = condition.get(varName).get("max")
        minVal = condition.get(varName).get("min")
    else:
        minVal = condition.get(varName).get("max")
        maxVal = condition.get(varName).get("min")

        if minVal is not None:
            minVal += 1
        else:
            maxVal -= 1

    (currMin, currMax) = range[rangeIndex]

    if maxVal is not None:
        if maxVal < currMin:
            return (False, None)
        if maxVal < currMax:
            fixedRangeForVar = (currMin, maxVal)
        else:
            fixedRangeForVar = (currMin, currMax)
    else:
        if minVal > currMax:
            return (False, None)
        if minVal > currMin:
            fixedRangeForVar = (minVal, currMax)
        else:
            fixedRangeForVar = (currMin, currMax)

    match varName:
        case "x":
            fixedRange = (fixedRangeForVar, range[1], range[2], range[3])
        case "m":
            fixedRange = (range[0], fixedRangeForVar, range[2], range[3])
        case "a":
            fixedRange = (range[0], range[1], fixedRangeForVar, range[3])
        case _:
            fixedRange = (range[0], range[1], range[2], fixedRangeForVar)
    return (compatible, fixedRange)

def findAcceptanceRangeForWorkflow(workflowName = "in", currentRanges = None, visitedWorkflows = []):
    
    acceptableRanges = []
    
    if workflowName in visitedWorkflows:
        print(workflowName, " already visited")
        return []

    visitedWorkflows.append(workflowName)

    if currentRanges is None:
        xRange = (1, 4000)
        mRange = (1, 4000)
        aRange = (1, 4000)
        sRange = (1, 4000)

        currentRanges = (xRange, mRange, aRange, sRange)
    
    workflow = workflows.get(workflowName)
    conds = workflow.get("conds")

    for i in range(len(conds) + 1):
        try:
            c = conds[i]
            d = c.get("dest")
        except:
            c = None
            d = workflow.get("finalLocation")

        (currCompatible, rangesForThisCond) = applyConditionToRange(c, currentRanges)
        (nextCompatible, currentRanges) = applyConditionToRange(c, currentRanges, True)

        if not currCompatible:
            continue

        if d == "A":
            acceptableRanges.append(rangesForThisCond)
        elif d == "R":
            continue
        else:
            acceptableRanges += findAcceptanceRangeForWorkflow(d, rangesForThisCond, visitedWorkflows)
        
        if not nextCompatible:
            break
        
    return acceptableRanges
    

def findAcceptableCombinationsForRange(range):
    res = 1

    for r in range:
        combosForVar = r[1] - r[0] + 1
        res *= combosForVar
    
    return res
