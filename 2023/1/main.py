import re

numberDictionary = {
       'one': '1',
       'two': '2',
       'three': '3',
       'four': '4',
       'five': '5',
       'six': '6',
       'seven': '7',
       'eight': '8',
       'nine' : '9'
}
part1 = 0
part2 = 0
with open("input.txt", "r") as f:
    lines = f.readlines()

def getNumberString (name):
    if numberDictionary.get(name) is not None:
           return numberDictionary.get(name)
    else:
           return name

for line in lines:
    allNumbers1 = re.findall(r'(?=(\d))', line)
    allNumbers2 = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line)

    number1 = allNumbers1[0] + allNumbers1[-1]
    number2 = getNumberString(allNumbers2[0]) + getNumberString(allNumbers2[-1])

    part1 += int(number1)
    part2 += int(number2)

print("part 1: ", part1)
print("part 2: ", part2)