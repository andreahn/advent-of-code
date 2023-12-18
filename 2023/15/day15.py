import re

with open("input.txt") as f:
    line = f.readline()
    line.strip()

sequences = line.split(",")

operationChars = ["-", "="]

def hashAlg(str):
    res = 0
    for c in str:
        asciiVal = ord(c)
        res += asciiVal
        res *= 17
        res %= 256
    return res


boxes = {
}

def placeInBox(box, label, focalLength):
    currentValuesInBox = boxes.get(box)
    
    if currentValuesInBox is None:
        boxes[box] = [label + ":" + focalLength]
    else:
        regex = re.compile(label + ":" + "\d+")
        currentForLabel = [s for s in currentValuesInBox if regex.match(s)]

        if len(currentForLabel) == 0:
            boxes[box].append(label + ":" + focalLength)
        else:
            currentForLabelIndex = currentValuesInBox.index(currentForLabel[0])
            boxes[box][currentForLabelIndex] = label + ":" + focalLength
        

def removeFromBox(box, str):
    currentValuesInBox = boxes.get(box)

    if box is None:
        return
    else:
        try:
            regex = re.compile(str + ":" + "\d+")
            currentForLabel = [s for s in currentValuesInBox if regex.match(s)]
            newArray = currentValuesInBox.copy()
            newArray.remove(currentForLabel[0])
            boxes[box] = newArray
        except:
            pass


def hashAlgAndPlaceInBox(str):
    boxVal = 0
    for i, c in enumerate(str):
        if c in operationChars:
            break
        asciiVal = ord(c)
        boxVal += asciiVal
        boxVal *= 17
        boxVal %= 256
    
    if c == "=":
        return placeInBox(boxVal, str[:i], (str[i+1:]))
    else:
        return removeFromBox(boxVal, str[:i])


def getFocusPowerOfLenses():
    sum = 0

    for box, boxContent in boxes.items():
        for i, val in enumerate(boxContent):
            focalLength = val[val.index(":") + 1:]
            sum += (box + 1) * (i + 1) * int(focalLength)

    return sum