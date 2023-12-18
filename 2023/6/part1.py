races_real = [
    {
        "time": 35,
        "distance": 213
    },
    {
        "time": 69,
        "distance": 1168
    },
    {
        "time": 68,
        "distance": 1086
    },
    {
        "time": 87,
        "distance": 1248
    }
]

races_sample = [
    {
        "time": 7,
        "distance": 9
    },
    {
        "time": 15,
        "distance": 40
    },
    {
        "time": 30,
        "distance": 200
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