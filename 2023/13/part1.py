from day13 import *

total_sum = 0

for i, pattern in enumerate(patterns):
    rows = findRowReflection(pattern)
    cols = findColumnReflection(pattern)

    if rows != -1:
        total_sum += rows * 100
    elif cols != -1:
        total_sum += cols

print(total_sum)