from day12 import *

sum = 0
for i, l in enumerate(inputData):
    s = l.get("s")
    newString = s + "?" + s + "?" + s + "?" + s + "?" + s
    newGroups = l.get("groups") * 5
    sum += part2Attempt2(newString, newGroups)

print(sum)
