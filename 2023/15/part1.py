from day15 import *

sum = 0
for s in sequences:
    sum += hashAlg(s)

print(sum)