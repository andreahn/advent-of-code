with open("input.txt", "r") as f:
    lines = f.readlines()


cards = {
    'A':13, 'K':12, 'Q':11, 'T':10, '9':9, '8':8, '7':7, '6':6, '5':5, '4':4, '3':3, '2':2, 'J':1
}

handTypes = ['fiveOfAKind', 'fourOfAKind', 'fullHouse', 'threeOfAKind', 'twoPair', 'onePair', 'highCard']

hands = []

def handType(hand):
    cardsInHand = {'A':0, 'K':0, 'Q':0, 'J':0, 'T':0, '9':0, '8':0, '7':0, '6':0, '5':0, '4':0, '3':0, '2':0}

    for card in hand:
        cardsInHand[card] = cardsInHand[card] + 1
    
    cardCounts = cardsInHand.values()
    cardsInHandExceptJokers = cardsInHand.copy()
    cardsInHandExceptJokers.pop("J")
    cardCountsExceptJokers = cardsInHandExceptJokers.values()


    jokerCount = cardsInHand.get("J")

    if 5 in cardCounts or (5 - jokerCount) in cardCountsExceptJokers:
        return 'fiveOfAKind'
    elif 4 in cardCounts or (4 - jokerCount) in cardCountsExceptJokers:
        return 'fourOfAKind'
    elif 3 in cardCounts:
        if 2 in cardCounts:
            return 'fullHouse'
        else:
            return 'threeOfAKind'
    elif (3 - jokerCount) in cardCountsExceptJokers:
        numberOfTwos = sum(1 for c in cardsInHandExceptJokers.values() if c == 2)
        realCountOfCard = (3 - jokerCount)

        if realCountOfCard == 2:
            if numberOfTwos > 1:
                return 'fullHouse'
            else:
                return 'threeOfAKind'
        else:
            if numberOfTwos > 0:
                return 'fullHouse'
            else:
                return 'threeOfAKind'
    elif 2 in cardCounts or (2 - jokerCount) in cardCountsExceptJokers:
        if len(list(filter(lambda x: x == 2, cardCounts))) > 1:
            return 'twoPair'
        else:
            return 'onePair'

    return 'highCard'

def customSort(toBeSorted, index = 0):
    sortedList = []

    for card in cards:
        handsWithCardsAtIndex = list(filter(lambda x: x.get("hand")[index] == card, toBeSorted))

        if len(handsWithCardsAtIndex) > 1:
            handsWithCardsAtIndex = customSort(handsWithCardsAtIndex, index + 1)
        
        sortedList += handsWithCardsAtIndex

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