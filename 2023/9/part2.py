with open("input.txt", "r") as f:
    lines = f.readlines()

allHistories = []

for line in lines:
    values = line.split(" ")
    values = [int(v.strip()) for v in values]

    allHistories.append(values)

def getDiffList (numbers):
    return [numbers[i + 1] - numbers[i] for i in range(0, len(numbers) - 1)]

def isAllZeroes(numbers):
    return len(list(filter(lambda x: x != 0 , numbers))) == 0


sum = 0

for history in allHistories:
    diffs = [history]
    
    listToGetDiffOf = history

    # Find initial diffs
    while True:
        tempDiff = getDiffList(listToGetDiffOf)
        diffs.append(tempDiff)

        if isAllZeroes(tempDiff):
            break
        else:
            listToGetDiffOf = tempDiff

    # Add values at end
    for diffIndex in range(len(diffs) - 1, -1, -1):
        currentDiff = diffs[diffIndex]

        if diffIndex == (len(diffs) - 1):
            # All zeros row
            valueToAdd = 0
        else:
            diffBelow = diffs[diffIndex + 1]
            valueToAdd = currentDiff[0] - diffBelow[0]
        
        newDiffToReplaceOld = [valueToAdd] + diffs[diffIndex]
        diffs[diffIndex] = newDiffToReplaceOld

    sum += diffs[0][0]

print(sum)