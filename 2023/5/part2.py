import re

# I'm not proud of this code, this is extremely slow 

with open("input.txt", "r") as f:
    lines = f.readlines()

currMap = ''
maps = {}

for index, line in enumerate(lines):

    # New map line
    mapName = re.findall(r'(.+) map:', line)
    if len(mapName) > 0:
        currMap = mapName[0]
        continue
    
    # Collect maps
    nums = re.findall(r'(\d+) (\d+) (\d+)', line)
    
    if len(nums) == 0 or currMap == '':
        continue

    nums = nums[0]

    currentValuesInMap = maps.get(currMap)
    # destination range start, the source range start, and the range length

    dictValue = {'destination': int(nums[0]), 'source': int(nums[1]), 'range': int(nums[2])}

    if currentValuesInMap is None:
        maps[currMap] = [dictValue]
    else:
        maps[currMap] = currentValuesInMap + [dictValue]

# Seeds
seedsVals = list(map(lambda x: int(x), lines[0].split(" ")[1:]))
seedRanges = []

for startIndex in range(0, len(seedsVals), 2):
    seedRanges.append({'start': seedsVals[startIndex], 'length': seedsVals[startIndex + 1]})

locationMaps = maps.get('humidity-to-location')
locationMaps.sort(key= lambda x : x.get("destination"))

def getSourceForDestination(target, mapVals):
    source = mapVals['source']
    range = mapVals['range']
    destination = mapVals['destination']

    if target >= destination and target <= destination + range:
        diff = target - destination
        return source + diff
    else:
        return None

def getSourcesFromDestinationAllMaps(target, mapVals):

    found = False
    res = []
    for map in mapVals:
        currRes = getSourceForDestination(target, map)

        if currRes is not None:
            found = True
            res.append(currRes)

    if found is False:
        return [target]
    return res

def findSeeds(location):

    seeds = []

    humiditities = getSourcesFromDestinationAllMaps(location, maps.get('humidity-to-location'))

    for h in humiditities:
        temperatures = getSourcesFromDestinationAllMaps(h, maps.get('temperature-to-humidity'))

        for t in temperatures:
            lights = getSourcesFromDestinationAllMaps(t, maps.get('light-to-temperature'))

            for l in lights:
                waters = getSourcesFromDestinationAllMaps(l, maps.get('water-to-light'))

                for w in waters:
                    fertilizers = getSourcesFromDestinationAllMaps(w, maps.get('fertilizer-to-water'))

                    for f in fertilizers:
                        soils = getSourcesFromDestinationAllMaps(f, maps.get('soil-to-fertilizer'))

                        for s in soils:
                            seed = getSourcesFromDestinationAllMaps(s, maps.get('seed-to-soil'))
                            seeds.append(seed)

    return seeds

def seedIsInRange(seed):
    global seedRanges

    for seedRange in seedRanges:
        if seed >= seedRange.get('start') and seed <= (seedRange.get('start') + seedRange.get('length')):
            return True
    
    return False

def findMinDestination():
    found = False
    dest = 0
    
    while found is False:
        dest += 1

        seeds = findSeeds(dest)

        for s in seeds:
            for seed in s:
                if seed is not None and seedIsInRange(seed):
                    return dest

print(findMinDestination())