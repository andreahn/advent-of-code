from day12 import *

sum = 0
for l in inputData:
    sum += part2Attempt2(l.get("s"), l.get("groups"))

print(sum)
