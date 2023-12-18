from day17 import *

shortestPaths = shortestPath(True)
res = float("inf")

for key, val in shortestPaths.items():
    if key.startswith(str(len(data) - 1) + ":" + str(len(data[0]) - 1)):
        if val < res:
            res = val

print(res)