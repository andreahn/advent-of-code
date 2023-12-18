with open("input.txt") as f:
    fileData = f.readlines()

data = []
for line in fileData:
    line = line.strip()
    nums = [*line]
    data.append([int(n) for n in nums])

def keyName (posx, posy, dir):
    return str(posx) + ":" + str(posy) + ":" + dir

def extractInfoFromKey (key):
    splitKey = key.split(":")
    return ((int(splitKey[0]), int(splitKey[1])), splitKey[2])

def getNeighbours(pos, dir, minSteps = 0, maxSteps = 3):
    (i, j) = pos
    res = []

    # Check straight down
    if dir != "d" and dir != "u":
        for k in range(i + minSteps + 1, i + maxSteps + 1):
            if k > len(data) - 1:
                break
            else:
                res.append(keyName(k, j, "d"))
    

    # Check straight up
    if dir != "d" and dir != "u":
        for k in range(i - maxSteps, i - minSteps):
            if k < 0:
                continue
            else:
                res.append(keyName(k, j, "u",))
    
    # Check straight left
    if dir != "l" and dir != "r":
        for l in range(j - maxSteps, j - minSteps):
            if l < 0:
                continue
            else:
                res.append(keyName(i, l, "l"))
    

    # Check straight right
    if dir != "l" and dir != "r":
        for l in range(j + minSteps + 1, j + maxSteps + 1):
            if l > len(data[0]) - 1:
                break
            else:
                res.append(keyName(i, l, "r"))
    return res

def getHeatLoss(notIncludedU, v):

    (i, j) = notIncludedU
    (k, l) = v

    if (i == k):
        line = data[i]

        if j < l:
            line = line[j + 1 : l + 1]
        else:
            line = line[l: j]
    else:
        line = [row[j] for row in data]

        if i < k:
            line = line[i + 1 : k + 1]
        else:
            line = line[k: i]

    total = sum(line)
    return total

def shortestPath(isPart2 = False):
    nodesToVisit = []
    height = len(data)
    width = len(data[0])

    iRange = range(height)
    jRange = range(width)

    distances = {}

    for i in iRange:
        for j in jRange:
            if i != 0:
                key = keyName(i, j, "d")
                distances[key] = float("inf")
                nodesToVisit.append(key)
            if i != height - 1:
                key = keyName(i, j, "u")
                distances[key] = float("inf")
                nodesToVisit.append(key)
            if j != 0:
                key = keyName(i, j, "r")
                distances[key] = float("inf")
                nodesToVisit.append(key)
            if j != width - 1:
                key = keyName(i, j, "l")
                distances[key] = float("inf")
                nodesToVisit.append(key)

    distances[keyName(0,0, "u")] = 0
    distances[keyName(0,0, "l")] = 0

    remainingDistances = distances.copy()

    while len(nodesToVisit) > 0:
        vKey = min(remainingDistances, key=remainingDistances.get)
        vDist = remainingDistances[vKey]
        nodesToVisit.remove(vKey)
        remainingDistances.pop(vKey)

        (vPos, vDir) = extractInfoFromKey(vKey)
        
        if isPart2:
            neighbours = getNeighbours(vPos, vDir, 3, 10)
        else:
            neighbours = getNeighbours(vPos, vDir)

        for uKey in neighbours:
            (uPos, uDir) = extractInfoFromKey(uKey)
            currUDist = distances[uKey]
            distanceBetweenNodes = getHeatLoss(vPos, uPos)
            altDist = vDist + distanceBetweenNodes

            if altDist < currUDist:
                distances[uKey] = altDist
                remainingDistances[uKey] = altDist
    
    return distances
