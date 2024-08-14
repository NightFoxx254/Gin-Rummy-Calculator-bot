import random
hand = [1,2,3,4,5,1,2,3,4,5]
for i in range(10):
    hand.append(random.randint(1,10))


def FindingConnections(hand):
    global handAfterFinder
    handAfterFinder = []

    #checking for pairs
    for i in range(10):
        if hand.count(hand[i]) == 2:
            print("yodee")
            for a in range(10):
                for b in range(10):
                    if a!=b:
                        if hand[a] == hand[i] and hand[b] == hand[i]:
                            for i in range(hand.count(hand[i])):
                                handAfterFinder.append(hand[i])
        if hand.count(hand[i]) == 3:
            print("beep")
            for a in range(10):
                for b in range(10):
                    for c in range(10):
                        if a!=b and b!=c and c!=a:
                            if hand[a] == hand[i] and hand[b] == hand[i] and hand[c] == hand[i]:
                                for i in range(hand.count(hand[i])):
                                    handAfterFinder.append(hand[i])
        if hand.count(hand[i]) == 4:
            print("meep")
            for a in range(10):
                for b in range(10):
                    for c in range(10):
                        for d in range(10):
                            if a!=b and b!=c and c!=d and d!=a:
                                if hand[a] == hand[i] and hand[b] == hand[i] and hand[c] == hand[i] and hand[d] == hand[i]:
                                    for i in range(hand.count(hand[i])):
                                        handAfterFinder.append(hand[i])

    print(handAfterFinder)

FindingConnections(hand)
