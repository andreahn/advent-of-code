races_real = [
    {
        "time": 35696887,
        "distance": 213116810861248
    }
]

races_sample = [
    {
        "time": 71530,
        "distance": 940200
    }
]

def getDistance(holdTime, totalTime):
    speed = holdTime
    timeToMove = totalTime - holdTime

    return speed * timeToMove

def findWaysToWinForGame(game):
    maxTime = game.get("time")
    recordDistance = game.get("distance")

    waysToWin = 0

    for t in range (0, maxTime):
        dist = getDistance(t, maxTime)

        if dist > recordDistance:
            waysToWin += 1
    
    return waysToWin

races = races_real
res = 1

for race in races:
    res *= findWaysToWinForGame(race)

print(res)