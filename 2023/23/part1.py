
# super slow solution... much improved version in part 2, but this is how i solved part 1

with open("input.txt", "r") as f:
    lines = f.readlines()

terrain = []

for i, l in enumerate(lines):
    terrain.append([*l.strip()])
    if i == 0:
        startPos = (i, l.index("."))
    elif i == len(lines) - 1:
        endPos = (i, l.index("."))

def getAllowedPositions(currPos, pathToNow):
    currX, currY = currPos
    res = []

    match terrain[currX][currY]:
        case "v":
            if (currX + 1, currY) not in pathToNow:
                res = [(currX + 1, currY)]
        case ">":
            if (currX, currY + 1) not in pathToNow:
                res = [(currX, currY + 1)]
        case _:
            if currX > 0 and (currX - 1, currY) not in pathToNow:
                res.append((currX - 1, currY))
                
            if currY > 0 and (currX, currY - 1) not in pathToNow:
                res.append((currX, currY - 1))

            if currX < len(terrain) and (currX + 1, currY) not in pathToNow:
                res.append((currX + 1, currY))

            if currY < len(terrain[0]) and (currX, currY + 1) not in pathToNow:
                res.append((currX, currY + 1))
    
    res = list(filter(lambda a: terrain[a[0]][a[1]] != "#", res))
    return res

def findPaths (currPos = startPos, pathToNow = [], currSteps = 0):

    currSteps += 1

    allowedNextPositions = getAllowedPositions(currPos, pathToNow)

    res = []

    currPath = pathToNow.copy()
    currPath.append(currPos)

    while len(allowedNextPositions) == 1:
        p = allowedNextPositions[0]
        if p == endPos:
            res.append(currSteps)
            return res
        else:
            currPos = p
            currPath.append(currPos)
            currSteps += 1
            allowedNextPositions = getAllowedPositions(currPos, currPath)

    for p in allowedNextPositions:
        if p == endPos:
            res.append(currSteps)
        else:
            temp = findPaths(p, currPath, currSteps)
            res += temp

    return res


res = findPaths()
print(max(res))