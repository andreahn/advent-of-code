from day19 import * 

getPart2Input()
ranges = findAcceptanceRangeForWorkflow()

sum = 0

for r in ranges:
    sum += findAcceptableCombinationsForRange(r)

print(sum)