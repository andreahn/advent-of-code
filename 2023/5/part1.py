import re

seeds = []

with open("input.txt", "r") as f:
    lines = f.readlines()


def toIntList (listToConvert):
    return list(map(lambda x: int(x), listToConvert))

def getDestination(target, mapVals):
    source = mapVals['source']
    range = mapVals['range']
    destination = mapVals['destination']

    if target >= source and target <= source + range:
        diff = target - source
        return destination + diff
    else:
        return None

def getDestinationFromMaps(target, mapVals):

    for map in mapVals:
        currRes = getDestination(target, map)

        if currRes is not None:
            return currRes
    return target

# Seeds
seeds = toIntList(lines[0].split(" ")[1:])

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
    dictValue = {'destination': int(nums[0]), 'source': int(nums[1]), 'range': int(nums[2])}

    if currentValuesInMap is None:
        maps[currMap] = [dictValue]
    else:
        maps[currMap] = currentValuesInMap + [dictValue]

locations = []

for seed in seeds:
    soil = getDestinationFromMaps(seed, maps.get('seed-to-soil'))
    fertilizer = getDestinationFromMaps(soil, maps.get('soil-to-fertilizer'))
    water = getDestinationFromMaps(fertilizer, maps.get('fertilizer-to-water'))
    light = getDestinationFromMaps(water, maps.get('water-to-light'))
    temperature = getDestinationFromMaps(light, maps.get('light-to-temperature'))
    humidity = getDestinationFromMaps(temperature, maps.get('temperature-to-humidity'))
    location = getDestinationFromMaps(humidity, maps.get('humidity-to-location'))
    locations.append(location)

print(min(locations))
