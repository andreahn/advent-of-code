
import re

with open("input.txt", "r") as f:
    lines = f.readlines()

terrain = []

for i, l in enumerate(lines):
    terrain.append([*l.strip()])
    if i == 0:
        startPos = (i, l.index("."))
    elif i == len(lines) - 1:
        endPos = (i, l.index("."))

nodes = {
      str(startPos): {
            "pos": startPos,
            "connections": {}
      },
      str(endPos): {
            "pos": endPos,
            "connections": {}
      }
}

def getAllPositions(currPos):
    currX, currY = currPos
    res = []

    if currX > 0:
        res.append((currX - 1, currY))
                
    if currY > 0:
        res.append((currX, currY - 1))

    if currX < len(terrain) - 1:
        res.append((currX + 1, currY))

    if currY < len(terrain[0]) - 1:
        res.append((currX, currY + 1))

    res = list(filter(lambda a:  terrain[a[0]][a[1]] != "#", res))
    
    return res

def getAllowedPositions(currPos, prevPos):
    currX, currY = currPos
    res = []

    if currX > 0 and (currX - 1, currY) != prevPos:
        res.append((currX - 1, currY))
                
    if currY > 0 and (currX, currY - 1) != prevPos:
        res.append((currX, currY - 1))

    if currX < len(terrain) - 1 and (currX + 1, currY) != prevPos:
        res.append((currX + 1, currY))

    if currY < len(terrain[0]) - 1 and (currX, currY + 1) != prevPos:
        res.append((currX, currY + 1))
    
    res = list(filter(lambda a: terrain[a[0]][a[1]] != "#", res))
    
    return res

searchedNodes = []


def findNodes ():
    global nodes
    global startPos
    global endPos

    nodesToSearch = [startPos, endPos]
    
    for i, l in enumerate(terrain):
        for j, c in enumerate(l):
            if c == "#":
                continue
            pos = (i, j)
            allowedPos = getAllPositions(pos)

            if len(allowedPos) > 2:
                nodesToSearch.append(pos)
                nodes[str(pos)] = {
                    "pos": pos,
                    "connections": {}
                }
                
    for node in nodesToSearch:
        startNodeDict = nodes.get(str(node))
        posFromNode = getAllPositions(node)

        for startPos in posFromNode:
            currPos = startPos
            allowedPos = getAllowedPositions(currPos, node)
            steps = 0

            while len(allowedPos) > 0:
                steps += 1

                if str(currPos) in nodes:
                    nextNodeInDict = nodes.get(str(currPos))
                    startNodeDict.get("connections")[str(currPos)] = steps
                    nextNodeInDict.get("connections")[str(node)] = steps
                    break
                else:
                    prevPos = currPos
                    currPos = allowedPos[0]
                    allowedPos = getAllowedPositions(currPos, prevPos)


def getTupleFromString(s):
    t = re.search(r"\((\d+), (\d+)\)", s)
    return (int(t.group(1)), int(t.group(2)))

max = 0
def findMaxPath (currNode = startPos, currPath = [], currSteps = 0):
    global max

    currNodeInDict = nodes.get(str(currNode))

    connections = currNodeInDict.get("connections")

    for connPos, dist in connections.items():
        connNode = getTupleFromString(connPos)

        if connNode in currPath:
            continue

        steps = currSteps + dist

        if connNode == endPos:
            if steps > max:
                max = steps
        else:
            newPath = currPath.copy()
            newPath.append(connNode)
            findMaxPath(connNode, newPath, steps)


findNodes()
findMaxPath()
print(max)