import re
with open("input.txt", "r") as f:
    lines = f.readlines()

nodes = {}
instructions = ""
currNode = "AAA"

for index, line in enumerate(lines):

    if index == 0:
        instructions = line.strip()
        continue

    temp = re.findall(r'([A-Z]+) = \(([A-Z]+), ([A-Z]+)\)', line)

    if len(temp) > 0:
        temp = temp[0]
        nodes[temp[0]] = {'L': temp[1], 'R': temp[2]}


complete = False
steps = 0

while complete is False:
    for step in instructions:
        currentNode = nodes.get(currNode)

        if step == "L":
            nextNode = currentNode.get("L")
        else:
            nextNode = currentNode.get("R")
        
        currNode = nextNode
        
        if nextNode == "ZZZ":
            complete = True
        steps += 1

print(steps)