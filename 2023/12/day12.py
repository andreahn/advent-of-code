import re

with open("input.txt") as f:
    lines = f.readlines()

inputData = []

possibilities = {}

for line in lines:
    splitLine = line.strip().split(" ")
    inputData.append({
        "s": splitLine[0],
        "groups": [int(num) for num in splitLine[1].split(",")]
    })

cache = {}

def getStringPlusGroupsKey (string, groups):
    return string + str(groups)

def part2Attempt2(stringToCheck, groups):
    totalPossibilities = 0

    keyInCache = getStringPlusGroupsKey(stringToCheck, groups)
    cachedRes = cache.get(keyInCache)

    if cachedRes is not None:
        return cachedRes
    else:
        firstGroup = groups[0]
        remainingGroups = groups[1:]

        firstGroupRegex = re.compile("[?#]{" + str(firstGroup) + "}")

        if len(remainingGroups) == 0:
            strFirstGroupMustFitIn = stringToCheck

            currFirstGroupStartIndex = 0
            currFirstGroupEndIndex = firstGroup

            while len(strFirstGroupMustFitIn) > 0:
                firstGroupMatch = re.search(firstGroupRegex, strFirstGroupMustFitIn)

                if firstGroupMatch is None:
                    break
                else:
                    [fromIndex, toIndex] = firstGroupMatch.span()

                    currFirstGroupStartIndex += fromIndex
                    currFirstGroupEndIndex += fromIndex

                    if "#" in stringToCheck[:currFirstGroupStartIndex]:
                        break
                    if "#" not in stringToCheck[currFirstGroupEndIndex:]:
                        totalPossibilities += 1

                    strFirstGroupMustFitIn = stringToCheck[currFirstGroupStartIndex + 1:]
                    currFirstGroupStartIndex += 1
                    currFirstGroupEndIndex += 1

        else:
            lenRemainingGroupsWithSeparators = len(remainingGroups) + sum(remainingGroups)

            strFirstGroupMustFitIn = stringToCheck[: -lenRemainingGroupsWithSeparators]

            currFirstGroupStartIndex = 0
            currFirstGroupEndIndex = firstGroup

            while len(strFirstGroupMustFitIn) > 0:

                firstGroupMatch = re.search(firstGroupRegex, strFirstGroupMustFitIn)

                if firstGroupMatch is None:
                    break
                else:
                    [fromIndex, toIndex] = firstGroupMatch.span()

                    currFirstGroupStartIndex += fromIndex
                    currFirstGroupEndIndex += fromIndex

                    if "#" in stringToCheck[:currFirstGroupStartIndex]:
                        break

                    if stringToCheck[currFirstGroupEndIndex] != "#":
                        
                        substringToFitRemainingGroups = stringToCheck[currFirstGroupEndIndex + 1:]
                        totalPossibilities += part2Attempt2(substringToFitRemainingGroups, remainingGroups)

                    strFirstGroupMustFitIn = strFirstGroupMustFitIn[fromIndex + 1:]
                    currFirstGroupStartIndex += 1
                    currFirstGroupEndIndex += 1

        cache[keyInCache] = totalPossibilities
        return totalPossibilities