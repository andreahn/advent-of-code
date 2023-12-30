import re
with open("input.txt", "r") as f:
    lines = f.readlines()

blocks = []

currName = chr(ord("A") - 1)
for l in lines:
    s = re.search(r'(\d+),(\d+),(\d+)~(\d+),(\d+),(\d+)', l)
    currName = chr(ord(currName) + 1)
    blocks.append({"name": currName, "pos": [[int(s.group(1)), int(s.group(2)), int(s.group(3))],
                   [int(s.group(4)), int(s.group(5)), int(s.group(6))]]})
blocks.sort(key = lambda x: min(x.get("pos")[0][2], x.get("pos")[1][2]))

blocksAfterFalling = {}

# Make blocks fall

for block in blocks:
    adjustedBlockPos = block.get("pos")
    currMinZ = min(adjustedBlockPos[0][2], adjustedBlockPos[1][2])
    supportingBlocks = []

    while currMinZ > 0:
        blocksOnSameLevel = dict(filter(lambda x: currMinZ - 1 == max(x[1].get("pos")[0][2], x[1].get("pos")[1][2]), blocksAfterFalling.items()))
        minX = min(adjustedBlockPos[0][0], adjustedBlockPos[1][0])
        maxX = max(adjustedBlockPos[0][0], adjustedBlockPos[1][0])
        minY = min(adjustedBlockPos[0][1], adjustedBlockPos[1][1])
        maxY = max(adjustedBlockPos[0][1], adjustedBlockPos[1][1])
        supportingBlocks = []
        blockName = block.get("name")


        for supportName, possibleSupportingBlock in blocksOnSameLevel.items():
            supportPos = possibleSupportingBlock.get("pos")
            minXS = min(supportPos[0][0], supportPos[1][0])
            maxXS = max(supportPos[0][0], supportPos[1][0])
            minYS = min(supportPos[0][1], supportPos[1][1])
            maxYS = max(supportPos[0][1], supportPos[1][1])

            overlapX = False
            overlapY = False

            # check X overlap
            if minX in range(minXS, maxXS + 1) or maxX in range(minXS, maxXS + 1):
                overlapX = True
            elif minX < minXS and maxX > maxXS:
                overlapX = True
            
            if not overlapX:
                continue
            
            # check Y overlap
            if minY in range(minYS, maxYS + 1) or maxY in range(minYS, maxYS + 1):
                overlapY = True
            elif minY < minYS and maxY > maxYS:
                overlapY = True
            
            if overlapY:
                supportingBlocks.append(supportName)
                if blocksAfterFalling.get(supportName) is None:
                    blocksAfterFalling[supportName] = {"supporting": [blockName]}
                else:
                    blocksAfterFalling.get(supportName)["supporting"].append(blockName)
        
        if len(supportingBlocks) > 0:
            break

        adjustedBlockPos[0][2] -= 1
        adjustedBlockPos[1][2] -= 1
        currMinZ -= 1

    if blocksAfterFalling.get(blockName) is None:
        blocksAfterFalling[blockName] = {"pos": adjustedBlockPos, "supportedBy": supportingBlocks, "supporting": []}
    else:
        blocksAfterFalling.get(blockName)["pos"] = adjustedBlockPos
        blocksAfterFalling.get(blockName)["supportedBy"] = supportingBlocks

sum = 0

# Find number of blocks that will fall if each block is removed

for i, b in blocksAfterFalling.items():
    fallingBlocksToCheck = set([])
    fallingBlocks = set([i])
    fallingBlocksToCheck = set(b.get("supporting"))
    prevLen = 0
    

    while prevLen != len(fallingBlocks):
        prevLen = len(fallingBlocks)
        newFallingBlocksToCheck = set([])

        for item in fallingBlocksToCheck:
            a = blocksAfterFalling.get(item)
            willFall = True
            
            for t in a.get("supportedBy"):
                if t not in fallingBlocks:
                    willFall = False
                    break
            
            if willFall:
                fallingBlocks.add(item)
                for j in a.get("supporting"):
                    newFallingBlocksToCheck.add(j)
        fallingBlocksToCheck = newFallingBlocksToCheck

    sum += len(fallingBlocks) - 1

print(sum)