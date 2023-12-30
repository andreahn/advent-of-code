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

blocksAfterFalling = []

criticalBlocks = set([])

for block in blocks:
    adjustedBlockPos = block.get("pos")
    currMinZ = min(adjustedBlockPos[0][2], adjustedBlockPos[1][2])
    supportingBlocks = []

    while currMinZ > 0:
        blocksOnSameLevel = list(filter(lambda x: currMinZ - 1 == max(x.get("pos")[0][2], x.get("pos")[1][2]), blocksAfterFalling))
        minX = min(adjustedBlockPos[0][0], adjustedBlockPos[1][0])
        maxX = max(adjustedBlockPos[0][0], adjustedBlockPos[1][0])
        minY = min(adjustedBlockPos[0][1], adjustedBlockPos[1][1])
        maxY = max(adjustedBlockPos[0][1], adjustedBlockPos[1][1])
        supportingBlocks = []


        for possibleSupportingBlock in blocksOnSameLevel:
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
                supportingBlocks.append(possibleSupportingBlock.get("name"))
        
        if len(supportingBlocks) > 0:
            if len(supportingBlocks) == 1:
                criticalBlocks.add(supportingBlocks[0])
            break

        adjustedBlockPos[0][2] -= 1
        adjustedBlockPos[1][2] -= 1
        currMinZ -= 1

    blocksAfterFalling.append({"name": block.get("name"), "pos": adjustedBlockPos, "supportedBy": supportingBlocks})

print(len(blocks) - len(criticalBlocks))