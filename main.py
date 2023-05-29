import copy

deck    = []
hands   = []

def getDeck():
    f = open("deck.mtgo", "r")
    for l in f:
        tab = l.split()
        if len(tab) == 0 or tab[0] == "SIDEBOARD:":
            return
        deck.append([int(tab[0]), "".join(tab[1:])])
    f.close()

def writeInFile():
    f = open("lines.txt", "w")
    for hand in hands:
        strHand = ""
        for card in hand:
            if type(card) is float:
                print(str(round(hand[-1], 4)) + strHand, file=f)
                continue
            strHand += " | "
            strHand = strHand + str(card[0]) + "x " + card[1]
    f.close()

def computeHands(hand = [], pos = 0, req = 7):
    if pos == len(deck):
        return
    rangeMax = min(req, deck[pos][0])
    hand.append([rangeMax + 1, deck[pos][1], pos])
    for instanceInHand in range(rangeMax, 0, -1):
        hand[-1][0] = hand[-1][0] - 1
        if req - instanceInHand == 0:
            hands.append(copy.deepcopy(hand))
        else:
            computeHands(hand, pos + 1, req - instanceInHand)
    hand.pop()
    computeHands(hand, pos + 1, req)

def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)

def computeOccurenceOfHands():
    for hand in hands:
        occurence=1
        for card in hand:
            occurence = occurence * int(fact(deck[card[2]][0]) / (fact(deck[card[2]][0] - card[0]) * fact(card[0])))
        hand.append(occurence)

def computePercentage():
    sum = 0
    for hand in hands:
        sum = sum + hand[-1]
    for hand in hands:
        hand[-1] = hand[-1] * 100000 / sum

def main():
    getDeck()
    computeHands()
    computeOccurenceOfHands()
    computePercentage()
    hands.sort(key = lambda x: x[-1], reverse=True)
    writeInFile()

main()