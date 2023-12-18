with open("input.txt", "r") as f:
    lines = f.readlines()


cards = {
    'A':13, 'K':12, 'Q':11, 'J':10, 'T':9, '9':8, '8':7, '7':6, '6':5, '5':4, '4':3, '3':2, '2':1
}

handTypes = ['fiveOfAKind', 'fourOfAKind', 'fullHouse', 'threeOfAKind', 'twoPair', 'onePair', 'highCard']

hands = []

def handType(hand):
    cardsInHand = {'A':0, 'K':0, 'Q':0, 'J':0, 'T':0, '9':0, '8':0, '7':0, '6':0, '5':0, '4':0, '3':0, '2':0}

    for card in hand:
        cardsInHand[card] = cardsInHand[card] + 1

    cardCounts = cardsInHand.values()

    if 5 in cardCounts:
        return 'fiveOfAKind'
    elif 4 in cardCounts:
        return 'fourOfAKind'
    elif 3 in cardCounts:
        if 2 in cardCounts:
            return 'fullHouse'
        else:
            return 'threeOfAKind'
    elif 2 in cardCounts:
        if len(list(filter(lambda x: x == 2, cardCounts))) > 1:
            return 'twoPair'
        else:
            return 'onePair'

    return 'highCard'

def customSort(toBeSorted, index = 0):
    sortedList = []

    for card in cards:
        temp = list(filter(lambda x: x.get("hand")[index] == card, toBeSorted))

        if len(temp) > 1:
            temp = customSort(temp, index + 1)
        
        sortedList += temp

    return sortedList

def findTotalForCardsOfType(handsToFindTotalFor, startRank):
    rank = startRank
    handsToFindTotalFor = customSort(handsToFindTotalFor)
    totalForCards = 0

    if handsToFindTotalFor is None:
        return [totalForCards, rank]

    for hand in handsToFindTotalFor:
        totalForCards += rank * int(hand.get('bid'))
        rank -= 1

    return [totalForCards, rank]

for line in lines:
    splitLine = line.split(" ")
    hand = splitLine[0].strip()
    bid = splitLine[1].strip()

    hands.append({
        'hand': hand,
        'bid': bid,
        'handType': handType(hand)
    })

total = 0
currentRank = len(hands)

for handType in handTypes:
    handsWithType = list(filter(lambda x: x.get("handType") == handType, hands))
    [temptotal, newrank] = findTotalForCardsOfType(handsWithType, currentRank)
    total += temptotal
    currentRank = newrank


print(total)
