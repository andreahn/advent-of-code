from day19 import *

getPart1Input()
acceptedParts = []

for p in parts:
    if partIsAccepted(p):
        acceptedParts.append(p)

sum = 0

for p in acceptedParts:
    sum += p.get("x")
    sum += p.get("m")
    sum += p.get("a")
    sum += p.get("s")

print(sum)